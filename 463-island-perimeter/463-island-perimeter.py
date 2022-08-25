class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        isValid = lambda r,c : 0<=r<len(grid) and 0<=c<len(grid[0])
        dirc = [0,1,0,-1,0]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    val = 4
                    for k in range(len(dirc)-1):
                        r,c = i + dirc[k],j+dirc[k+1]
                        if isValid(r,c) and grid[r][c] == 1:
                            val -= 1
                    ans += val
        return ans