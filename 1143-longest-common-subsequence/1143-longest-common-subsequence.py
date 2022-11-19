class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def lcs(idx1,idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            ans = 0
            if text1[idx1] == text2[idx2]:
                ans = 1 + lcs(idx1+1,idx2+1)
            else:
                ans = max(lcs(idx1+1,idx2),lcs(idx1,idx2+1))
            return ans
        return lcs(0,0)