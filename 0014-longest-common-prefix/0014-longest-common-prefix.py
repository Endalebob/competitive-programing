class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 200
        for i in strs:
            j = min(j,len(i))
        for k in range(j):
            i = 0
            word = strs[0][k]
            while i < len(strs):
                if strs[i][k] != word:
                    return strs[0][:k]
                i += 1
        return strs[0][:j]
                