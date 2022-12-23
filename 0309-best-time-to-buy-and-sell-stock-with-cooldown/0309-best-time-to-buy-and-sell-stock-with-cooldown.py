class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(idx,flag):
            if idx >= len(prices):
                return 0
            if flag:
                return max(dp(idx+1,1-flag)-prices[idx],dp(idx+1,flag))
            return max(dp(idx+2,1-flag)+prices[idx],dp(idx+1,flag))
        return dp(0,1)