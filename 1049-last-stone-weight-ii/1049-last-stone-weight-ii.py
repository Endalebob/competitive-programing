class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def dp(idx,s):
            if idx == len(stones):
                return abs(s)
            return min(dp(idx+1,s+stones[idx]),dp(idx+1,s-stones[idx]))
        return dp(0,0)