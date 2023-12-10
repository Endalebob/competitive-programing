class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        @lru_cache(None)
        def dp(tot):
            if tot == 0:
                return 1
            if tot < 0:
                return 0
            ans = 0
            for i in nums:
                ans += dp(tot-i)
            return ans
        return dp(target)