class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        isvalid = lambda r,c: 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == "1"
        dirc = ((0,1),(0,-1),(1,0),(-1,0))
        def dfs(i,j):
            grid[i][j] = "0"
            for dr,dc in dirc:
                r,c = i+dr,j+dc
                if isvalid(r,c):
                    dfs(r,c)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        return ans