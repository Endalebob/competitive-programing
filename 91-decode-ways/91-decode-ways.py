class Solution:
    def numDecodings(self, s: str) -> int:
        dic = set(str(i) for i in range(1,27))
        dp = {}
        def rec(l):
            if l == len(s):
                return 1
            if l in dp:
                return dp[l]
            ans = 0
            if s[l:l+1] in dic:
                ans += rec(l+1)
            if s[l:l+2] in dic:
                ans += rec(l+2)
            dp[l] = ans
            return ans
        return rec(0)