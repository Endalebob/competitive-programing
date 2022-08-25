class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sums = sum(nums)
        left = 0
        for i in range(len(nums)):
            sums -= nums[i]
            if left == sums: return i
            left += nums[i]
            
        return -1