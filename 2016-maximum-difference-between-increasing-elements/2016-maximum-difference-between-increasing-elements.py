class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        minimum = nums[0]
        for i in range(1,len(nums)):
            ans = max(ans,nums[i]-minimum)
            minimum = min(minimum,nums[i])
        return ans if ans > 0 else -1
        