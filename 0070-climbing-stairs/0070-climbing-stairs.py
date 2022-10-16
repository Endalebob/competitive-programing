class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,2
        ans = n
        for i in range(3,n+1):
            ans = a+b
            a,b = b,ans
        return ans
            