class Solution:
    def calculateMinimumHP(self, d: List[List[int]]) -> int:
        n,mm = len(d),len(d[0])
        @lru_cache(None)
        def is_possible(r,c,val):
            if val<1:
                return False
            if r == n-1 and c == mm-1:
                return val+d[r][c] > 0
            if r>=n or c>=mm:
                return False
            new_val = val + d[r][c]
            return is_possible(r+1,c,new_val) or is_possible(r,c+1,new_val)
        l,r = 1,10**9
        ans = r
        while l<=r:
            m = l + (r-l)//2
            if is_possible(0,0,m):
                ans = min(m,ans)
                r = m-1
            else:
                l = m+1
        return ans