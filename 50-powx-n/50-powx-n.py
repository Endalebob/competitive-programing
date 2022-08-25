class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n *= -1
            x = 1/x
        if n%2 == 0:
            return self.myPow(x,n//2)**2
        return x*self.myPow(x,n//2)**2
        