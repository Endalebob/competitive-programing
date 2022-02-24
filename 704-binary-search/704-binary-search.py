class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        left = 0
        middle = (right + left)//2
        while right >= left:
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
                middle = (right + left)//2
            else:
                left = middle + 1
                middle = (right + left)//2
        return -1