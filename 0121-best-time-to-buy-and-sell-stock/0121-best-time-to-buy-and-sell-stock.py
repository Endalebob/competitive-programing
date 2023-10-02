class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = prices[0]
        ans = 0
        for i in prices:
            max_ = min(i,max_)
            ans = max(ans,i-max_)
        return ans