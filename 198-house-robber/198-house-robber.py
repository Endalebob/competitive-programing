class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def rec(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = nums[i] + max(rec(i+3),rec(i+2))
            return memo[i]
        return max(rec(0),rec(1))
        