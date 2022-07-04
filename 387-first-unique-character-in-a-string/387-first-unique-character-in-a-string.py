class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrence = defaultdict(int)
        for i in s:
            occurrence[i]+=1
        for i in range(len(s)):
            if occurrence[s[i]] == 1:
                return i
        return -1