class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def baseb(n, b):
            e = n//b
            q = n%b
            if n == 0:
                return '0'
            elif e == 0:
                return str(q)
            else:
                return baseb(e, b) + str(q)
        if n<1:
            return False
        ternary = baseb(n,3)
        return n>0 and ternary.count('1') == 1 and '2' not in  ternary