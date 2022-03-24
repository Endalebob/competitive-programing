class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        while left<len(nums):
            minn = nums[left]
            maxx = nums[left]
            for right in range(left,len(nums)):
                if nums[right]<minn: minn = nums[right]
                if nums[right]>maxx: maxx = nums[right]
                ans += (abs(minn-maxx))
            left += 1
        return ans