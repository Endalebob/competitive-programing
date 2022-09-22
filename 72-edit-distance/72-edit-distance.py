class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dic(i,j):
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if word1[i] == word2[j]:
                return dic(i+1,j+1)
            else:
                return min(dic(i+1,j+1),dic(i,j+1),dic(i+1,j))+1
        return dic(0,0)