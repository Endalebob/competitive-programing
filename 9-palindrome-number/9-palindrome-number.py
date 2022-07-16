class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l,r = 0,len(x)-1
        while l<r:
            if x[l] != x[r]:
                return False
            r -= 1
            l += 1
        return True