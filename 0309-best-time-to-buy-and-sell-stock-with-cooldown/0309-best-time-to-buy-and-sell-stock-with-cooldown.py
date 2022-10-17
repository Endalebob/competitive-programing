class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1][1], dp[-1][2])