class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1]*len(nums)
        def dp(idx):
            if idx == len(nums)-1:
                return True
            elif idx>=len(nums):
                return False
            if memo[idx] != -1:
                return memo[idx]
            curr = idx+nums[idx]
            for i in range(idx+1,min(len(nums),idx+nums[idx]+1)):
                if i+nums[i] > curr:
                    curr = i+nums[i] 
                    if dp(i):
                        memo[idx] = True
                        return True
                elif i == len(nums)-1:
                    memo[idx] = True
                    return True
            memo[idx] = False
            return False
        return dp(0)