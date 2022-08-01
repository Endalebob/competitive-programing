class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1,0,-1):
            ans += max(0,prices[i]-prices[i-1])
        return ans