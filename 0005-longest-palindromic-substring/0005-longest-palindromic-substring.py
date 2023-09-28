class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_pal(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        ans = 1
        ret = s[0]
        i = 0
        for i in range(len(s)-1):
            for j in range(len(s)-1,i+ans-1,-1):
                if is_pal(i,j):
                    ans = j-i+1
                    ret = s[i:j+1]
                    break
        return ret
            
            