class Solution:
    def canMeasureWater(self, j1: int, j2: int, t: int) -> bool:
        if j1+j2 < t:
            return False
        if t % j1 == 0 or t % j2 == 0:
            return True
        if gcd(j1,j2) == 1:
            return True
        return False