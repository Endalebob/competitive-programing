class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            ans = max(prices[i]-mi,ans)
            mi = min(mi,prices[i])
        return ans
        
        