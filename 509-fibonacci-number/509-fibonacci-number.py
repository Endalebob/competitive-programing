class Solution:
    def fibb(self, n: int,dic) -> int:
        if n in dic:
            return dic[n]
        else:
            dic[n] = self.fibb(n-1,dic) + self.fibb(n-2,dic)
        return dic[n]
    def fib(self, n: int) -> int:
        dic = {0: 0, 1: 1}
        return self.fibb(n,dic)