class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        r = 0
        while len(prices)>r:
            k = r
            while len(prices)>r+1 and prices[r]-1 == prices[r+1]:
                r += 1
            n = r-k+1
            ans += n*(n+1)//2
            r+=1
        return ans
            
        