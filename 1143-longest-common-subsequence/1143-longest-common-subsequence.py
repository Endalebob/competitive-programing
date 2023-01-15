class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        if I find the same letter I add them if I didn't I have two options 
        the first is to delete the letter from text1 and the second option is
        to delete from the second. I try both and I take the one that generate
        maximum LCS.
        '''
        memo = {}
        def dp(idx1,idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            if (idx1,idx2) in memo:
                return memo[(idx1,idx2)]
            if text1[idx1] == text2[idx2]:
                memo[(idx1,idx2)] = 1 + dp(idx1+1,idx2+1)
            else:
                memo[(idx1,idx2)] = max(dp(idx1+1,idx2),dp(idx1,idx2+1))
            return memo[(idx1,idx2)]
        return dp(0,0)
        