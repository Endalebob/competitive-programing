class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        @cache
        def rec(l,r):
            if l == r:
                return 1
            if l>r:
                return 0
            if s[l] == s[r]:
                return 2+rec(l+1,r-1)
            return max(rec(l+1,r),rec(l,r-1))
        return rec(0,len(s)-1)
                    