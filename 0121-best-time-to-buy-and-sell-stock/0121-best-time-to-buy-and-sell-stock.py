class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = sell = prices[0]
        for i in range(1,len(prices)):
            sell = max(sell,prices[i])
            ans = max(ans,sell-buy)
            if buy > prices[i]:
                sell = buy = prices[i]
        return ans
        