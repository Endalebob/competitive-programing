class Solution:
    def findOrder(self, c: int, pre: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i,j in pre:
            graph[i].append(j)
        vstd = set()
        ans = []
        def dfs(node):
            if node in cycle:
                return False
            if node in vstd:
                return True
            cycle.add(node)
            for i in graph[node]:
                if not dfs(i):
                    return False
            cycle.remove(node)
            vstd.add(node)
            ans.append(node)
            return True
        for i in range(c):
            cycle = set()
            if not dfs(i):
                return []
        return ans
        