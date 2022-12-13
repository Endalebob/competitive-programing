class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dirc = [[1,0],[1,1],[1,-1]]
        is_valid = lambda c :0<=c<n
        @lru_cache(None)
        def dp(r,c):
            if r == n:
                return 0
            ans = 10**6
            for i,j in dirc:
                nr,nj = i+r,j+c
                if is_valid(nj):
                    ans = min(ans,dp(nr,nj)+matrix[r][c])
            return ans
        ans = 10**6
        for i in range(n):
            ans = min(ans,dp(0,i))
        return ans