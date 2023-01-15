class Solution:
    def countArrangement(self, n: int) -> int:
        '''
        take a sit and relax an know this fact God is in control
        check every possibilities. and track which num you use.
        '''
        
        @lru_cache(None)
        def dp(idx,include):
            if idx == n+1:
                return 1
            ans = 0
            for i in include:
                if idx%i and i%idx:
                    continue
                new = tuple(j for j in include if j != i)
                ans += dp(idx+1,new)
            return ans
        return dp(1,tuple(i for i in range(1,n+1)))
                    
        