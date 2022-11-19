class Solution:
    def change(self, a: int, c: List[int]) -> int:
        vstd = set()
        c.sort()
        memo = {}
        def dp(s,idx):
            if s == a:
                return 1
            if s>a:
                return 0
            if (s,idx) in memo:
                return memo[(s,idx)]
            ans = 0
            for i in range(idx,len(c)):
                if c[i]+s > a:
                    break
                ans += dp(s+c[i],i)
            memo[(s,idx)] = ans
            return ans
        return dp(0,0)