class Solution:
    def ans(self,n,dic):
        if n in dic:
            return dic[n]
        dic[n] = self.ans(n-1,dic)+self.ans(n-2,dic)
        return dic[n]
    def climbStairs(self, n: int) -> int:
        dic = {1:1,2:2}
        return self.ans(n,dic)
        