class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def knapsack(s):
            if s == amount:
                return 0
            elif s>amount:
                return float('inf')
            ans = float('inf')
            for i in coins:
                ans = min(knapsack(s+i),ans)
            return ans + 1
        ret = knapsack(0)
        return ret if ret != float('inf') else -1