class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        isValid = lambda r,c: 0<=r<len(grid) and 0<=c<len(grid[0])
        next = [0,1,0,-1,0]
        def dfs(r,c):
            grid[r][c] = '#'
            for i in range(4):
                rr,cc=r+next[i],c+next[i+1]
                if isValid(rr,cc) and grid[rr][cc] == '1':
                    dfs(rr,cc)
                
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans