class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(idx):
            if idx > n:
                return 0
            if idx == n:
                return 1
            if idx in memo:
                return memo[idx]
            memo[idx] = dp(idx+1) + dp(idx+2)
            return memo[idx]
        return dp(0)
