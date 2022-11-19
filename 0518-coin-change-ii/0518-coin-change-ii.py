class Solution:
    def change(self, a: int, c: List[int]) -> int:
        vstd = set()
        memo = {}
        def dp(s,idx):
            if s == a:
                return 1
            if idx >= len(c) or s>a:
                return 0
            if (s,idx) in memo:
                return memo[(s,idx)]
            memo[(s,idx)] = dp(s+c[idx],idx)+dp(s,idx+1)
            return memo[(s,idx)]
        return dp(0,0)