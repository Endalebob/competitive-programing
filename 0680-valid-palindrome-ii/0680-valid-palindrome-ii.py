class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispal(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        cnt = 0
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                if not (ispal(i,len(s)-i-2) or (ispal(i+1,len(s)-i-1))):
                    return False
                return True
        return True