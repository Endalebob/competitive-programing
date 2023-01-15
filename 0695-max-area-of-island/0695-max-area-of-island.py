class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        path = [[0,1],[1,0],[0,-1],[-1,0]]
        n,m = len(grid),len(grid[0])
        is_valid = lambda r,c : 0<=r<n and 0<=c<m and (r,c) not in vstd and grid[r][c]
        
        def dfs(r,c):
            vstd.add((r,c))
            ans = 1
            for x_dir,y_dir in path:
                if is_valid(r+x_dir,c+y_dir):
                    ans += dfs(r+x_dir,c+y_dir)
            return ans
        ans = 0
        vstd = set()
        for i in range(n):
            for j in range(m):
                if is_valid(i,j):
                    ans = max(ans,dfs(i,j))
        return ans
        