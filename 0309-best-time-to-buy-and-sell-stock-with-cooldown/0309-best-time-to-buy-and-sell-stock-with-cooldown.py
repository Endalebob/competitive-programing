class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(idx,state):
            if idx>=len(prices):
                return 0
            if state == 1:
                ans = 0
                for i in range(idx,len(prices)):
                    if prices[idx]>=prices[i] and i-idx>3:
                        break
                    ans = max(ans,prices[i]+dp(i+2,0))
            else:
                ans = 0
                for i in range(idx,len(prices)):
                    if prices[idx]<=prices[i] and i-idx>3:
                        break
                    ans = max(ans,-prices[i]+dp(i+1,1))
            return ans
        return dp(0,0)