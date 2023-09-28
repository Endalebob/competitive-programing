class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(idx,curr):
            if curr > amount or idx >= len(coins):
                return inf
            if curr == amount:
                return 0
            return min(dp(idx,curr+coins[idx])+1,dp(idx+1,curr))
        val = dp(0,0)
        return val if val != inf else -1