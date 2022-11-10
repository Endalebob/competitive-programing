class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        m = 0
        while i<len(nums):
            new_i = i+1
            while new_i<len(nums) and nums[i] == nums[new_i]:
                m+=1
                nums[new_i] = 111
                new_i += 1
            i = new_i
        nums.sort()
        while nums[-1] == 111:
            nums.pop()