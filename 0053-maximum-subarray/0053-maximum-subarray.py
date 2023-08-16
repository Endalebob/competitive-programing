class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = 0
        ans = -float('inf')
        for i in nums:
            running_sum += i
            ans = max(ans,running_sum)
            running_sum = max(running_sum,0)
        return ans