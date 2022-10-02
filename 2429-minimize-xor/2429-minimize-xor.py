class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ans = format(num1,'b').zfill(30)
        nm2 = format(num2,'b').count('1')
        nn = format(num1,'b').count('1')
        res = nm2-nn
        if res == 0:
            return int(ans,2)
        a = 0
        if res > 0:
            for i in range(30):
                if ans[-i-1] == '0':
                    a += 2**i
                    res -= 1
                if res == 0:
                    break
            return int(ans,2) + a
        for i in range(30):
            if ans[-i-1] != '0':
                a -= 2**i
                res += 1
            if res == 0:
                break
        return int(ans,2) + a   
        