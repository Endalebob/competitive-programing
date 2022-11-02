class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right,left = [1],[1]
        for i in nums:
            left.append(left[-1]*i)
        for i in nums[::-1]:
            right.append(right[-1]*i)
        right = right[::-1]
        for i in range(len(nums)):
            nums[i] = right[i+1]*left[i]
        return nums