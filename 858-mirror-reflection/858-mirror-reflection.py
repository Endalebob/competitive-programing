class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def rec(dr,val,sign):
            if val == p and dr == 0:
                return 1
            if val == p and dr == 1:
                return 2
            if val == 0 and dr == 0:
                return 0
            if sign == 1:
                val += q
                if val > p:
                    val = (2*p-val)
                    sign = 0
            else:
                val -= q
                if val<0:
                    val = -val
                    sign = 1
            return rec(1-dr,val,sign)
        return rec(1,0,1)
                