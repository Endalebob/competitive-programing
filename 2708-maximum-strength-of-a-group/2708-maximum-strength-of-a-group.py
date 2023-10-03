class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        curr = min_max = nums[0]
        while i<len(nums) and nums[i] < 0:
            curr *= nums[i]
            min_max = max(min_max,curr)
            i += 1
        i = 2
        curr = max_max = nums[-1]
        while i<=len(nums) and nums[-i] > 0:
            curr *= nums[-i]
            max_max = max(max_max,curr)
            i += 1
        if nums[0] < 0 and nums[-1] >= 0:
            return max(min_max*max_max,min_max,max_max)
        if nums[0] < 0:
            return min_max
        return max_max