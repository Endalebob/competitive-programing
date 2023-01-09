class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def is_in_range(x1,y1,x2,y2,r):
            return (x1-x2)**2 + (y1-y2)**2 <= r**2
        graph = defaultdict(set)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if is_in_range(bombs[i][0],bombs[i][1],bombs[j][0],bombs[j][1],bombs[i][2]):
                    graph[i].add(j)
        def dfs(node):
            if node in vstd:
                return 0
            vstd.add(node)
            ans = 1
            for i in graph[node]:
                ans += dfs(i)
            return ans
        ans = 1
        for i in range(len(bombs)):
            vstd = set()
            ans = max(ans,dfs(i))
        return ans