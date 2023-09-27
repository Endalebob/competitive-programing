class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dp(idx):
            if idx > n:
                return 0
            if idx == n:
                return 1
            return dp(idx+1) + dp(idx+2)
        return dp(0)