class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def dp(c,k):
            if k <= 0 or c >= len(piles):
                return 0
            ans = dp(c+1,k)
            hold = 0
            for i in range(len(piles[c])):
                if k-i <= 0:
                    return ans
                hold += piles[c][i]
                ans = max(ans,dp(c+1,k-i-1)+hold)
            return ans
        return dp(0,k)