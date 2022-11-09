class Solution:
    def wordBreak(self, s: str, word: List[str]) -> bool:
        @lru_cache(None)
        def dp(idx):
            if idx == len(s):
                return True
            for i in word:
                if idx + len(i) <= len(s):
                    if s[idx:idx+len(i)] == i:
                        if dp(idx+len(i)):
                            return True
            return False
        return dp(0)