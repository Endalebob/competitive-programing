class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        l,r = 0,x+1
        while l<r:
            mid = (l+r)//2

            if mid**2 > x:
                r = mid
            if mid**2 <= x:
                ans = mid
                l = mid+1
        return ans