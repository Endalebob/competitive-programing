class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(idx,curr):
            if curr == amount:
                return 0
            if curr > amount or idx>=len(coins):
                return inf
            if (idx,curr) not in memo:
                memo[idx,curr] = min(dp(idx+1,curr),dp(idx,curr+coins[idx])+1)
            return memo[idx,curr]
        ans = dp(0,0)
        if ans != inf:
            return ans
        return -1