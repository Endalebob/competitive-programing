class Solution:
    def reverse(self, x: int) -> int:
        if x <0:
            x = str(x)
            a = x[1:]
            b = a[::-1]
            ans = -int(b)
            if ans<-2**31:
                return 0
            return ans
        x = str(x)
        a = x[::-1]
        ans = int(a)
        if ans>=2**31:
            return 0
        return ans