class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,max(1,x)
        while l<r:
            m = l + (r-l)//2
            if m*m < x:
                l = m+0.0001
            else:
                r = m
        return int(l)