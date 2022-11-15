class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        @lru_cache(None)
        def dp(n):
            if n == 0: return 1
            ans = 0
            for i in range(1,n+1):
                if i < 3:
                    ans += dp(n-i)
                else:
                    ans += 2*dp(n-i)
            return ans % mod
        return dp(n)%mod