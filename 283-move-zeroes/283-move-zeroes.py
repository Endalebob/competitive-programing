class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        len_nums = len(nums)
        i = 0
        while i < (len_nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                i -= 1
                len_nums -= 1
            i += 1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        