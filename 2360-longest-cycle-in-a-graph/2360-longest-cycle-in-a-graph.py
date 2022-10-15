class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        for i,v in enumerate(edges):
            graph[v].append(i)
        vstd = set()
        self.ans = -1
        def dfs(node):
            # print(cycle)
            if node in cycle:
                self.ans = max(self.ans,len(cycle))
                return True
            if node in vstd:
                return True
            cycle.add(node)
            for i in graph[node]:
                dfs(i)
            cycle.remove(node)
            vstd.add(node)
            return True
        for i in range(len(edges)):
            cycle = set()
            dfs(i)
        return self.ans