class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph1= defaultdict(set)
        graph2 = defaultdict(list)
        out_degree = defaultdict(int)
        for fro,to in edges:
            graph1[to].add(fro)
            graph2[fro].append(to)
            out_degree[to] += 1
        ans = []
        deq = deque()
        for i in range(n):
            if not graph1[i]: deq.append(i)
        while deq:
            curr = deq.popleft()
            for i in graph2[curr]:
                out_degree[i] -= 1
                graph1[i] = graph1[i].union(graph1[curr])
                if out_degree[i] == 0:
                    deq.append(i)
        return [sorted(graph1[i]) for i in range(n)]