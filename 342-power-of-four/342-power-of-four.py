class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n%4 != 0 and n != 1:
            return False
        elif n<=0:
            return False
        elif n==1:
            return True
        return self.isPowerOfFour(n//4)