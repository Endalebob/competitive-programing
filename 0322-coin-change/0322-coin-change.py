class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(idx,tot):
            if tot > amount or idx >= len(coins):
                return float('inf')
            if tot == amount:
                return 0
            return min(dp(idx+1,tot),dp(idx,tot+coins[idx])+1)
        ans = dp(0,0)
        return ans if ans != float('inf') else -1