class Solution:
    def romanToInt(self, s: str) -> int:
        rTi = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        state = 1
        s = s[::-1]
        for i in s:
            if rTi[i]>=state:
                state = rTi[i]
                ans += rTi[i]
            else:
                ans -= rTi[i]
        return ans
                