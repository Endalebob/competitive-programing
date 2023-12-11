class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 0
        l,r = 0,len(nums)-1
        while r>l:
            m = (r+l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        return nums[l]