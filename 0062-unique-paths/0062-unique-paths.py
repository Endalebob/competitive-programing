class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache(None)
        def dp(r,c):
            if r == m-1 and c == n-1:
                return 1
            if r >= m or c >= n:
                return 0
            return dp(r+1,c) + dp(r,c+1)
        return dp(0,0)