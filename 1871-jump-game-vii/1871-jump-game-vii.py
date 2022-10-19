class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[0] == '1' or s[-1] == '1':
            return False
        @lru_cache(None)
        def dp(idx):
            if idx == len(s)-1:
                return True
            k = minJump
            for i in range(min(idx+1 + maxJump, len(s))-1,idx+minJump-1,-1):
                if s[i] == '0':
                    k -= 1
                    if dp(i):
                        return True
                    if not k:
                        return False
            return False
        return dp(0)