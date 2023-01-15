class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        if I find the same letter I add them if I didn't I have two options 
        the first is to delete the letter from text1 and the second option is
        to delete from the second. I try both and I take the one that generate
        maximum LCS.
        '''
        memo = defaultdict(int)
        for idx1 in range(len(text1)-1,-1,-1):
            for idx2 in range(len(text2)-1,-1,-1):
                if text1[idx1] == text2[idx2]:
                    memo[(idx1,idx2)] = 1 + memo[(idx1+1,idx2+1)]
                else:
                    memo[(idx1,idx2)] = max(memo[(idx1+1,idx2)],memo[(idx1,idx2+1)])
        return memo[(0,0)]
                
                
        