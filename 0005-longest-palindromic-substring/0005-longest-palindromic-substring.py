class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        def is_valid(l,r):
            val = ''
            while l>=0 and r<len(s) and s[l] == s[r]:
                val = s[l:r+1]
                l -=1
                r += 1
            return val
        for i in range(len(s)):
            ans = max(is_valid(i,i),is_valid(i,i+1),ans,key=len)
        return ans
            
            