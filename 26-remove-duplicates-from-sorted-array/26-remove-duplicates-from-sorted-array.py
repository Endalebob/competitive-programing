class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = len(nums)-1
        i = 0
        while i<m:
            if nums[i]==nums[i+1]:
                nums.pop(i)
                m -=1
                i -= 1
            i += 1
        return len(nums)