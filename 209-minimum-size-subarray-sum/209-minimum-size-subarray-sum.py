class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        ans = len(nums)+1
        summ = 0
        while r<len(nums):
            summ += nums[r]
            while summ>=target:
                ans = min(ans,r-l+1)
                summ -= nums[l]
                l+=1
            r+=1
        return ans%(len(nums)+1)
                