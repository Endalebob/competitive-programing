class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        @lru_cache(None)
        def ispal(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        @lru_cache(None)
        def dp(l,r):
            if r >= len(s) or r-l > k:
                return 0
            if ispal(l,r):
                return 1+dp(r+1,r+k)
            return max(dp(l+1,r+1),dp(l,r+1))
        return dp(0,k-1)