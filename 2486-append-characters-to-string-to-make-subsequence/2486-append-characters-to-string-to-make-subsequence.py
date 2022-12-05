class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx = 0
        for i in range(len(t)):
            temp = idx
            for j in range(idx,len(s)):
                if s[j] == t[i]:
                    idx = j+1
                    break
            if idx == temp:
                return len(t)-i
        return 0