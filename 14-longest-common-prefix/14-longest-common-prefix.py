class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for i in range(len(strs[0])):
            for j in strs:
                if len(j) == i:
                    return j
                if strs[0][i] != j[i]:
                    return j[:i]
        return strs[0]
                    