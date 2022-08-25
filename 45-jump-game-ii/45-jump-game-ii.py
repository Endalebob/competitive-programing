class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def dp(ind):
            if ind>=len(nums)-1:
                return 0
            jumps=float("inf")
            
            for i in range(1,nums[ind]+1):
                jumps=min(jumps,1+dp(ind+i))
              
            return jumps
        
        return dp(0)