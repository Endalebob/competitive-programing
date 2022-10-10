class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        isvalid = lambda r,c: 0<=r<len(grid) and 0<=c<len(grid[0])
        dirc = [[0,1],[1,0],[0,-1],[-1,0]]
        k,kk = 0,0
        n = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    k,kk = i,j
                elif grid[i][j] == 0:
                    n += 1
        def dfs(i,j):
            if (i,j) in vstd or grid[i][j] == -1:
                return 0
            if grid[i][j] == 2 and n+1 == len(vstd):
                return 1
            vstd.add((i,j))
            ans = 0
            for ii,jj in dirc:
                r,c = ii+i,jj+j
                if isvalid(r,c) and grid[r][c] != -1:
                    ans += dfs(r,c)
            vstd.remove((i,j))
            return ans
        vstd = set()
        return dfs(k,kk)
            