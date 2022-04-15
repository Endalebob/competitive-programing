class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vstd = set()
        ans = 0
        def dfs(i):
            vstd.add(i)
            for j in range(len(isConnected[i])):
                if j not in vstd and isConnected[i][j] == 1:
                    dfs(j)
        for i in range(len(isConnected)):
            if i not in vstd:
                ans += 1
                dfs(i)
        return ans