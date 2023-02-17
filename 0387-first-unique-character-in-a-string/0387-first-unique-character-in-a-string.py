class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeat = Counter(s)
        for i in range(len(s)):
            if repeat[s[i]] == 1:
                return i
        return -1
        