class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        dirc = [[0,1],[1,0],[-1,0],[0,-1]]
        is_valid = lambda r,c : 0<=r<n and 0<=c<m
        mod = 10**9 + 7
        @lru_cache(None)
        def dp(r,c):
            ans = 1
            for i,j in dirc:
                nr,nc = r+i,c+j
                if is_valid(nr,nc) and grid[nr][nc] > grid[r][c]:
                    ans += dp(nr,nc)
            return ans % mod
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += dp(i,j)
        return ans % mod