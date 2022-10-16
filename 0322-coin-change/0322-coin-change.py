class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for k in coins:
                if i-k >= 0:
                    dp[i] = min(dp[i],dp[i-k]+1)
                else:
                    break
        return dp[amount] if dp[amount]<10**5 else -1