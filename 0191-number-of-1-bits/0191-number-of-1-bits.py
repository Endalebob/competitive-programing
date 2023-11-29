class Solution:
    def hammingWeight(self, n: int) -> int:
        def binn(n):
            nn = len(format(n,'b'))
            Ans = 0
            for I in range(nn):
                if 1&(n>>I):
                    Ans +=1
            return Ans
        return binn(n)
            