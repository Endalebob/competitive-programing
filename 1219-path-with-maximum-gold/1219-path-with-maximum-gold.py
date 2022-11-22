class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        
        is_valid = lambda r,c : 0<=r<n and 0<=c<m and grid[r][c] != 0
        dirc = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def dfs(r,c):
            ans = 0
            for dx,dy in dirc:
                new_x,new_y = dx+r,dy+c
                if is_valid(new_x,new_y) and (new_x,new_y) not in vstd:
                    vstd.add((new_x,new_y))
                    ans = max(ans,grid[new_x][new_y]+dfs(new_x,new_y))
                    vstd.remove((new_x,new_y))
            return ans
        ret = 0
        vstd = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    vstd.add((i,j))
                    ret = max(ret,grid[i][j]+dfs(i,j))
                    vstd.remove((i,j))
        return ret