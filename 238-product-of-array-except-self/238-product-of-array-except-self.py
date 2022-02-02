class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side_mul = [1]*len(nums)
        right_side_mul = [1]*len(nums)
        left_side,right_side = 1,1
        for i in range(1,len(nums)):
            left_side *= nums[i-1]
            right_side *= nums[-i]
            left_side_mul[i] = left_side
            right_side_mul[-i-1] = right_side
        for i in range(len(nums)):
            nums[i] = right_side_mul[i] * left_side_mul[i]
        return nums