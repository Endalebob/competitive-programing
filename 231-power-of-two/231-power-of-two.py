class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        temp = n
        count = -1
        while temp > 0:
            temp >>= 1
            count += 1
        n &= ~(1<<count)
        return n == 0