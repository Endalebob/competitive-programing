class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0,cost[0]]
        for i in range(1,len(cost)):
            ans.append(cost[i]+min(ans[-1],ans[-2]))
        return min(ans[-1],ans[-2])