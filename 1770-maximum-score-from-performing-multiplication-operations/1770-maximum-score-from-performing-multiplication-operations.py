class Solution:
    def maximumScore(self, nums: List[int], mul: List[int]) -> int:
        dp = [0] * (len(mul) + 1)
        for m in range(len(mul) - 1, -1, -1):
            pd = [0] * (m + 1)
            for l in range(m, -1, -1):
                pd[l] = max(dp[l + 1] + mul[m] * nums[l], 
                            dp[l] + mul[m] * nums[~(m - l)])
            dp = pd
        return dp[0]
        # # @lru_cache(None)
        # dp = {}
        # def knapsack(idx,l,r):
        #     if idx>=len(m):
        #         return 0
        #     if (l,r) in dp:
        #         return dp[(l,r)]
        #     left = nums[l]*m[idx]+knapsack(idx+1,l+1,r)
        #     right = nums[r]*m[idx]+knapsack(idx+1,l,r-1)
        #     dp[(l,r)] =  max(left,right)
        #     return dp[(l,r)]
        # return knapsack(0,0,len(nums)-1)
        # m,n = len(multipliers),len(nums)
        # dp=[[0]*(m+1) for i in range(m+1)]
        # for j in range(m-1, -1, -1):
        #     for low in range(j, -1, -1):
        #         first=nums[low]*multipliers[j]+dp[j+1][low+1]
        #         last=nums[n-1-(j-low)]*multipliers[j]+dp[j+1][low]
        #         dp[j][low]=max(first, last)
        # return dp[0][0]