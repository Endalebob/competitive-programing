class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(grid[0]))] for j in range(len(grid))]
        dp[0][0] = grid[0][0]
        dirc = [[0,-1],[-1,0]]
        isvalid = lambda r,c : 0<=r<len(grid) and 0<=c<len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for ii,jj in dirc:
                    r,c = i+ii,j+jj
                    if isvalid(r,c):
                        dp[i][j] = min(dp[i][j],dp[r][c]+grid[i][j])
        return dp[-1][-1]