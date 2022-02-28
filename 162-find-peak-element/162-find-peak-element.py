class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        middle = (right + left)//2
        while left<right:
            if nums[middle] > nums[middle+1] and nums[middle] > nums[middle-1]:
                return middle
            elif nums[middle] > nums[middle+1]:
                right = middle
                middle = (right + left)//2
            else:
                left = middle + 1
                middle = (right + left)//2
        return middle
        