class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(idx):
            if idx>len(cost)-1: return 0
            return min(dp(idx+1),dp(idx+2))+cost[idx]
        return min(dp(0),dp(1))