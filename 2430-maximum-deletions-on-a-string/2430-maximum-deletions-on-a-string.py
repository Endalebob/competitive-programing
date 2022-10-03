class Solution:
    def deleteString(self, s: str) -> int:
        @lru_cache(None)
        def rec(idx):
            if len(set(s[idx:])) == 1:
                return len(s[idx:])
            # if idx==len(s)-1: return 1
            if idx >= len(s): return 0
            ans = 1
            for i in range(idx+1,idx+(len(s)-idx)//2+1):
                v = i-idx
                if s[idx:i] == s[i:v+i]:
                    ans = max(ans,1+rec(idx+v))
            return ans
        return rec(0)