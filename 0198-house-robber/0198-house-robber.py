class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(idx):
            if idx >= len(nums):
                return 0
            return max(nums[idx]+dp(idx+2),dp(idx+1))
        return dp(0)