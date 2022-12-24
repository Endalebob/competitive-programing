class Solution:
    def numTilings(self, n: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n == 0: return 1
            ans = 0
            for i in range(1,n+1):
                if i >= 3:
                    ans += 2*dp(n-i)
                else:
                    ans += dp(n-i)
            return ans % (10**9+7)
        return dp(n)