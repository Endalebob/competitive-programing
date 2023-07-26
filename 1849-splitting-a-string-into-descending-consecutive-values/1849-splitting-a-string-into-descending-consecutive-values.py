class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def rec(idx,cnt,prev):
            if idx == n:
                return cnt >= 2
            for i in range(idx,n):
                new = int(s[idx:i+1])
                if cnt == 0 or prev-1 == new:
                    if rec(i+1,cnt+1,new):
                        return True
            return False
        return rec(0,0,-1)