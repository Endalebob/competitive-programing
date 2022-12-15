class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dp(idx1,idx2):
            if idx1 == len(text1) or idx2 == len(text2):
                return 0
            if text1[idx1] == text2[idx2]:
                return 1 + (dp(idx1+1,idx2+1))
            return max(dp(idx1+1,idx2),dp(idx1,idx2+1))
        return dp(0,0)