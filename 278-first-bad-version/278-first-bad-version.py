# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r,m = 0,n,n//2
        while l<r-1:
            if m == r:
                return m
            if isBadVersion(m):
                r = m
            else:
                l = m
            m = (r+l)//2
        return r