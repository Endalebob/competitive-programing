class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n,m = len(grid),len(grid[0])
        def dfs(r,c):
            if c == m or c == -1:
                return -1
            if r>=n:
                return c
            if c > 0 and grid[r][c] == -1:
                if grid[r][c-1] == 1:
                    return -1
            else:
                if c<m-1 and grid[r][c+1] == -1:
                    return -1
            if grid[r][c] == -1:
                return dfs(r+1,c-1)
            else:
                return dfs(r+1,c+1)
        ans = []
        for j in range(m):
            ans.append(dfs(0,j))
        return ans