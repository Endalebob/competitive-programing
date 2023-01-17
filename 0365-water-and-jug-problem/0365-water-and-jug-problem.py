class Solution:
    def canMeasureWater(self, j1: int, j2: int, tc: int) -> bool:
        if j1+j2<tc:
            return False
        def gcd(a,b):
            if a == 0:
                return b
            return gcd(b%a,a)
        return tc % (gcd(j1,j2)) == 0