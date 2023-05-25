class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        ran_ge = len(nums) - 4
        if len(nums) < 5:
            return 0
        ans = float('inf')
        for i in range(len(nums)-ran_ge):
            ans = min(ans,nums[i+ran_ge]-nums[i])
        return ans
            
            