class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)-1
        ans = 0
        while nums[i-2]+nums[i-1]<=nums[i] and i>1:
            i -= 1
        if i == 1:
            return ans
        return nums[i]+nums[i-1]+nums[i-2]