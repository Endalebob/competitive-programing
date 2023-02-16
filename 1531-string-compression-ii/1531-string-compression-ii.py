class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(idx, prev_char, length, k):
            if k < 0:
                return float('inf')
            if idx >= len(s):
                return 0
            delete = dp(idx+1, prev_char, length, k-1)
            keep = 0
            if s[idx] == prev_char:
                if length in [1, 9, 99]:
                    keep = 1
                keep += dp(idx+1, prev_char, length+1, k)
            else:
                keep = 1 + dp(idx+1, s[idx], 1, k)
            return min(delete, keep)

        return dp(0, '', 0, k)