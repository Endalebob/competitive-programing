# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = (left+right)//2
        while left<right:
            if isBadVersion(mid) == True:
                right = mid
                mid = (left+right)//2
            else:
                left = mid+1
                mid = (left+right)//2
        print(left,right)
        return mid