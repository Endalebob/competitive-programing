class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        
        is_valid = lambda r,c : 0<=r<n and 0<=c<m and grid[r][c] != 0
        dirc = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(r,c,cnt):
            self.tot = max(self.tot,cnt)
            ans = 0
            for dx,dy in dirc:
                new_x,new_y = dx+r,dy+c
                if is_valid(new_x,new_y):
                    original = grid[new_x][new_y]
                    grid[new_x][new_y] = 0
                    ans = max(ans,original+dfs(new_x,new_y,cnt+1))
                    grid[new_x][new_y] = original
            return ans
        
        ret = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    self.tot = 0
                    ori = grid[i][j]
                    grid[i][j] = 0
                    ret = max(ret,ori+dfs(i,j,1))
                    grid[i][j] = ori
                    if self.tot == min(m*n,25):
                        return ret
        return ret