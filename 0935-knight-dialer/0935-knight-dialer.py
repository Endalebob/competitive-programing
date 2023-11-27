class Solution:
    def knightDialer(self, n: int) -> int:
        move = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        isvalid = set([(i,j) for i in range(4) for j in range(3)])
        isvalid.remove((3,0))
        isvalid.remove((3,2))
        @lru_cache(None)
        def dp(i,j,rem):
            if rem <= 0:
                return 1
            ans = 0
            for di,dj in move:
                ni,nj = di+i,dj+j
                if (ni,nj) in isvalid:
                    ans += dp(ni,nj,rem-1)
            return ans % (10**9+7)
        ans = 0
        for i,j in isvalid:
            ans += dp(i,j,n-1)
            ans %= (10**9+7)
        return ans % (10**9+7)
            