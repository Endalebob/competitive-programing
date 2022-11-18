class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -float('inf')
        curr = 0
        for i in nums:
            curr = max(i,curr+i)
            best = max(best,curr)
        return best