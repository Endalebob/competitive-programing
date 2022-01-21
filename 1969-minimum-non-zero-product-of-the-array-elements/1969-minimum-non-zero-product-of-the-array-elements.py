class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        m = pow(2,p)-2
        n = pow(2,(p-1))-1
        mod = pow(10,9)+7
        an = pow(m,n,mod)
        l = pow(2,p)-1
        ans = (an*l)%mod
        return ans