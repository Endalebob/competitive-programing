class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-9]*amount
        def knapsack(s):
            if s == amount:
                return 0
            elif s>amount:
                return float('inf')
            if memo[s] != -9:
                return memo[s]
            ans = float('inf')
            for i in coins:
                ans = min(knapsack(s+i),ans)
            memo[s] = ans + 1
            return ans + 1
        ret = knapsack(0)
        return ret if ret != float('inf') else -1