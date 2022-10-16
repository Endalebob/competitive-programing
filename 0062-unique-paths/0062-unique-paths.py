class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        isvalid = lambda r,c : 0<=r<n and 0<=c<m
        dirc = [[0,-1],[-1,0]]
        dp = [[0 for i in range(m)] for j in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                for ii,jj in dirc:
                    r,c = ii+i,j+jj
                    if isvalid(r,c):
                        dp[i][j] += dp[r][c]
        return dp[n-1][m-1]