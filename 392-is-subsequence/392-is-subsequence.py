class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        @cache
        def dp(idx,st):
            if st == s:
                return True
            if len(st) >= len(s):
                return False
            if idx == len(t):
                return False
            if s[len(st)] == t[idx] and dp(idx+1,st+t[idx]):
                return True
            return dp(idx+1,st)
        return dp(0,'')