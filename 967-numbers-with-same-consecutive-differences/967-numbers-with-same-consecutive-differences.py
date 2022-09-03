class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        def rec(c):
            if len(c) == n:
                if c[0] != 0:
                    ans.append(int(c))
                return
            if int(c[-1])-k >= 0:
                rec(c+str(int(c[-1])-k))
            if int(c[-1])+k < 10:
                rec(c+str(int(c[-1])+k))
        for i in range(1,10):
            rec(str(i))
        return set(ans)