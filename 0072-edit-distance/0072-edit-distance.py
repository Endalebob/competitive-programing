class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(idx1,idx2):
            if idx2 == len(word2):
                return len(word1)-idx1
            if idx1 == len(word1):
                return len(word2) - idx2
            if word1[idx1] == word2[idx2]:
                return dp(idx1+1,idx2+1)
            return min(dp(idx1,idx2+1),dp(idx1+1,idx2),dp(idx1+1,idx2+1)) + 1
        return dp(0,0)