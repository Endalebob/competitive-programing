class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def rec(num):
            if num<=1:
                return num == 1
            return rec(num/4)
        return rec(n)