class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        ans = n
        for i in range(2,n+1):
            ans = a+b
            a,b = b,ans
        return ans