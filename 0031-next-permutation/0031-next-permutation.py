class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        idx = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                idx = i
                break
        if idx == -1:
            reverse(0,n-1)
            return nums
        for i in range(n-1,0,-1):
            if nums[i] > nums[idx]:
                nums[idx],nums[i] = nums[i],nums[idx]
                break
        reverse(idx+1,n-1)
        return nums