class Solution:
    def removePalindromeSub(self, s: str) -> int:
        for i in range(len(s)//2):
            if s[i] != s[-1-i]: return 2
        return 1