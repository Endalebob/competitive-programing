class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(curr):
            if curr > target:
                return 0
            if curr == target:
                return 1
            ans = 0
            for i in nums:
                ans += dp(curr+i)
            return ans
        return dp(0)