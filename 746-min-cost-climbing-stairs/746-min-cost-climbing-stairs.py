class Solution:
    def costs(self,cost,i,dic):
        if i>=len(cost):
            return 0
        if i in dic: 
            return dic[i]
        else:
            dic[i] = cost[i] + min(self.costs(cost,i+1,dic),self.costs(cost,i+2,dic))
            return dic[i]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dic = {}
        return min(self.costs(cost,0,dic),self.costs(cost,1,dic))