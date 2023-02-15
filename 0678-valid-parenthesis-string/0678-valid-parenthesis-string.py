class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)
        def rec(idx,ope):
            if idx == len(s):
                if ope == 0:
                    return True
                return False
            if ope < 0:
                return False
            if s[idx] == '(':
                return rec(idx+1,ope+1)
            if s[idx] == ')':
                return rec(idx+1,ope-1)
            return rec(idx+1,ope-1) or rec(idx+1,ope) or rec(idx+1,ope+1)
        return rec(0,0)