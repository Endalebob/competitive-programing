class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def rec(idx,part,prev):
            if idx == n:
                return part >= 2
            for i in range(idx,n):
                new = int(s[idx:i+1])
                if prev == '+' or prev-1 == new:
                    if rec(i+1,part+1,new):
                        return True
            return False
        return rec(0,0,'+')