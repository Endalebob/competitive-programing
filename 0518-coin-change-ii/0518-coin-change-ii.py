class Solution:
    def change(self, a: int, c: List[int]) -> int:
        vstd = set()
        @lru_cache(None)
        def dp(s,idx):
            if s == a:
                return 1
            if idx >= len(c) or s>a:
                return 0
            return dp(s+c[idx],idx)+dp(s,idx+1)
        return dp(0,0)