class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = ''
        while a != b and a != 0 and b!=0:
            if a>b:
                a-=2
                b-=1
                s += 'aab'
            else:
                b-=2
                a-=1
                s += 'bba'
        if a == 0:
            return s+'b'*b
        if b == 0:
            return s+'a'*a
        return s+'ab'*a
        