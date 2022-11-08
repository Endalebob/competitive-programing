class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        root = 0
        vstd = set()
        def dfs(root):
            vstd.add(root)
            val = 0
            for i in graph[root]:
                if i not in vstd:
                    val += dfs(i)
            if val:
                return val+1
            if hasApple[root]:
                return 1
            return val
        return max(0,2*(dfs(root)-1))