class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        l,r = 0,x+1
        mid = (l+r)//2
        while l<r:
            if mid**2 > x:
                r = mid
            if mid**2 <= x:
                ans = mid
                l = mid+1
            mid = (l+r)//2
        return ans