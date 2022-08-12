class Solution:
    def isPerfectSquare(self, x: int) -> bool:
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
        return ans**2 == x