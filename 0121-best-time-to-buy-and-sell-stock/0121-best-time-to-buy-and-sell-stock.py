class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        m = prices[0]
        for i in range(1,len(prices)):
            m = min(m,prices[i])
            ans = max(ans,prices[i]-m)
        return ans
        