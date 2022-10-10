class Solution:
    def uniquePathsWithObstacles(self, ob: List[List[int]]) -> int:
        isvalid = lambda r,c: 0<=r<len(ob) and 0<=c<len(ob[0])
        dirc = [[0,1],[1,0]]
        @lru_cache(None)
        def dfs(i,j):
            if ob[i][j] == 1:
                return 0
            if i == len(ob)-1 and j == len(ob[0])-1:
                return 1
            ans = 0
            for ii,jj in dirc:
                r,c = ii+i,jj+j
                if isvalid(r,c) and ob[r][c] == 0:
                    ans += dfs(r,c)
            return ans
        return dfs(0,0)