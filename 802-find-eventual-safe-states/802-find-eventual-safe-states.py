class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited,cycle,ans = set(),set(),[]
        def dfs(idx):
            if idx in cycle:
                return False
            if idx in visited:
                return True
            cycle.add(idx)
            for i in graph[idx]:
                if dfs(i) == False:
                    return False
            cycle.remove(idx)
            visited.add(idx)
            ans.append(idx)
        for i in range(len(graph)):
            dfs(i)
        ans.sort()
        return ans