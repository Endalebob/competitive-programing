class Solution:
    def fib(self, n: int) -> int:
        A=(1+5**0.5)/2
        B=(1-5**0.5)/2
        fi = ((pow(A,n) - pow(B,n))) // sqrt(5)
        return int(fi)