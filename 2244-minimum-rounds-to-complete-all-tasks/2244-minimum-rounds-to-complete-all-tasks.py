class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks)
        nums = list(c.values())
        @lru_cache(None)
        def dp(curr,idx):
            if idx == len(nums)-1 and curr == 0:
                return 0
            if curr < 0:
                return float('inf')
            if curr == 0:
                return dp(nums[idx+1],idx+1)
            return min(dp(curr-3,idx)+1,dp(curr-2,idx)+1)
        ans = dp(nums[0],0)
        return ans if ans < float('inf') else -1