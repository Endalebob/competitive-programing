class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        index = 0
        minn = [prices[0],0]
        maxx = [prices[1],1]
        ans = 0
        while index+1<len(prices):
            if prices[index+1]>=maxx[0] or maxx[1]<=minn[1]:
                maxx = [prices[index+1],index+1]
            if prices[index]<=minn[0]:
                minn = [prices[index],index]
            if maxx[1]>=minn[1]:
                ans = max(maxx[0]-minn[0],ans)
            index += 1
        return ans