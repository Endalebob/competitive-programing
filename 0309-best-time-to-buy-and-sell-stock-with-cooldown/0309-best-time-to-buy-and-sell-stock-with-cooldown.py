class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        for idx in range(len(prices)-1,-1,-1):
            for state in [0,1]:
                if state == 1:
                    ans = 0
                    for i in range(idx,len(prices)):
                        if prices[idx]>=prices[i] and i-idx>3:
                            break
                        ans = max(ans,prices[i]+memo[(i+2,0)])
                else:
                    ans = 0
                    for i in range(idx,len(prices)):
                        if prices[idx]<=prices[i] and i-idx>3:
                            break
                        ans = max(ans,-prices[i]+memo[(i+1,1)])
                memo[(idx,state)] = ans

        return memo[(0,0)]