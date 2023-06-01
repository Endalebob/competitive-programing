class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def dp(idx,turn):
            if idx == len(prices):
                return 0
            if turn:
                return max(dp(idx+1,1-turn)-prices[idx]-fee,dp(idx+1,turn))
            return max(dp(idx+1,1-turn)+prices[idx],dp(idx+1,turn))
        return dp(0,1)