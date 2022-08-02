class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ans = [[float('inf') for _ in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    ans[i][j] = grid[i][j]
                elif i == 0:
                    ans[i][j] = ans[i][j-1]+grid[i][j]
                elif j == 0:
                    ans[i][j] = ans[i-1][j]+grid[i][j]
                else: 
                    ans[i][j] = min(ans[i-1][j],ans[i][j-1])+grid[i][j]
        return ans[-1][-1]