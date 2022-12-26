class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(idx):
            if idx == len(nums)-1:
                return True
            elif idx>=len(nums):
                return False
            curr = idx+nums[idx]
            for i in range(idx+1,min(len(nums),idx+nums[idx]+1)):
                if i+nums[i] > curr:
                    curr = i+nums[i] 
                    if dp(i):
                        return True
                elif i == len(nums)-1:
                    return True
            return False
        return dp(0)