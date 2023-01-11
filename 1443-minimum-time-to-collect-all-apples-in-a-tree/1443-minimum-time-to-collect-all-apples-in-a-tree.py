class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        vstd = set()
        def dfs(node,depth):
            vstd.add(node)
            ans = 0
            for i in graph[node]:
                if i not in vstd:
                    ans += dfs(i,depth+1)
            if ans or hasApple[node]:
                return ans + 2
            return ans
        return max(0,dfs(0,0)-2)
            