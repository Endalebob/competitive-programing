class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        row,col = len(grid),len(grid[0])
        isvalid = lambda r,c: 0<=r<row and 0<=c<col
        dirc = [[1,0],[0,1]]
        @lru_cache(None)
        def dfs(i,j):
            if i == row-1 and j == col-1:
                m = defaultdict(int)
                m[grid[i][j]%k] += 1
                return m
            
            ans = defaultdict(int)
            for ii,jj in dirc:
                r,c = ii+i,jj+j
                if isvalid(r,c):
                    m = dfs(r,c)
                    for key in m:
                        value = m[key]
                        new_key = (key+grid[i][j])%k
                        ans[new_key] += value
            return ans
        return dfs(0,0)[0]% (10**9+7)