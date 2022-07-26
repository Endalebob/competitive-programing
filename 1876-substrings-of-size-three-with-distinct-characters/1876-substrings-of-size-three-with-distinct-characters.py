class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-2):
            sett=set()
            sett.add(s[i])
            sett.add(s[i+1])
            sett.add(s[i+2])
            if len(sett) == 3:
                ans += 1
        return ans
        