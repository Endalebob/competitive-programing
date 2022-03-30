class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        right = len(nums)-1
        left = 0
        middle = (right + left)//2
        while right >= left:
            if nums[middle] == target:
                left = right = middle
                while right<len(nums)-1 and nums[right+1] == nums[middle]:
                    right += 1
                while left>0 and nums[left-1] == nums[middle]:
                    left -= 1
                return [left,right]

            elif nums[middle] > target:
                right = middle - 1
                middle = (right + left)//2
            else:
                left = middle + 1
                middle = (right + left)//2
        return [-1,-1]