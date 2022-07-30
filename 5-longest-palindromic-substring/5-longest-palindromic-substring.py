class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l,r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return l,r
        check = 0
        ans = s[0]
        for i in range(len(s)-1):
            l,r = helper(i,i)
            if r-l-1>check:
                check = r-l-1
                ans = s[l+1:r]
            l,r = helper(i,1+i)
            if r-l-1>check:
                check = r-l-1
                ans = s[l+1:r]
        return ans
            