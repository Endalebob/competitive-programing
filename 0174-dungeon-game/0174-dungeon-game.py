class Solution:
    def calculateMinimumHP(self, d: List[List[int]]) -> int:
        n,mm = len(d),len(d[0])
        ispossible = lambda r,c : 0<=r<n and 0<=c<mm
        @lru_cache(None)
        def is_possible(r,c):
            if r == n-1 and c == mm-1:
                return min(d[-1][-1],0)
            ans = -float('inf')
            if ispossible(r+1,c):
                ans = max(ans,is_possible(r+1,c))
            if ispossible(r,c+1):
                ans = max(ans,is_possible(r,c+1))
            return min(0,ans+d[r][c])
        return 1-is_possible(0,0)  