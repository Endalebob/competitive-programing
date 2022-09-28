class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        val = 0
        l,r = 0,0
        ans = 0
        while r<len(nums):
            while val & nums[r] != 0:
                ans = max(ans,r-l)
                val ^= nums[l]
                l+=1
            val |= nums[r]
            r += 1

        return max(ans,r-l)