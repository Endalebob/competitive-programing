class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        relation = defaultdict(list)
        graph = defaultdict(list)
        for i in range(len(routes)):
            for j in routes[i]:
                if relation[j]:
                    for k in relation[j]:
                        graph[k].append(i)
                        graph[i].append(k)
                relation[j].append(i)
            routes[i] = set(routes[i])
        deq = []
        vstd = set()
        for i in relation[source]:
            deq.append((i,1))
            vstd.add(i)
        deq = deque(deq)
        while deq:
            if source == target:
                return 0
            node,cost = deq.popleft()
            if target in routes[node]:
                return cost
            for i in graph[node]:
                if i not in vstd:
                    vstd.add(i)
                    deq.append((i,cost+1))
        return -1
        