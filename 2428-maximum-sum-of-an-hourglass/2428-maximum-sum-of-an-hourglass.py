class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def tot(r,c):
            ans = grid[r+1][c+1]
            for i in range(3):
                if i != 1:
                    for j in range(3):
                        ans += grid[i+r][c+j]
            return ans
        ret = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                ret = max(ret,tot(i,j))
        return ret
        