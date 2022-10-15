class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        graph = defaultdict(int)
        out_degree = defaultdict(list)
        deq = deque()
        for i in p:
            graph[i[0]] += 1
            out_degree[i[1]].append(i[0])
        for i in range(n):
            if not graph[i]:
                deq.append(i)
        while deq:
            curr = deq.popleft()
            for i in out_degree[curr]:
                graph[i] -= 1
                if graph[i] == 0:
                    deq.append(i)
            n -= 1
        return n == 0
        