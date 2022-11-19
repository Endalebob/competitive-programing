class Solution:
    def change(self, a: int, c: List[int]) -> int:
        vstd = set()
        c.sort()
        @lru_cache(None)
        def dp(s,idx):
            if s == a:
                return 1
            if s>a:
                return 0
            ans = 0
            for i in range(idx,len(c)):
                if c[i]+s > a:
                    break
                ans += dp(s+c[i],i)
            return ans
        return dp(0,0)