class Solution:
    def fib(self, n: int) -> int:
        dic = {}
        def rec(n):
            if n == 0 or n == 1:
                return n
            if n in dic:
                return dic[n]
            dic[n] = rec(n-1)+rec(n-2)
            return dic[n]
        return rec(n)
    
        