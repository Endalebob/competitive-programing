class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, sr: int, sc: int) -> int:
        move = [(1,0),(0,1),(-1,0),(0,-1)]
        is_valid = lambda r, c : 0<=r<m and 0<=c<n
        
        @lru_cache(None)
        def dfs(r,c,k):
            if k == 0:
                return k
            ans = 0
            for i,j in move:
                new_r,new_c = r+i,j+c
                if is_valid(new_r,new_c):
                    ans += dfs(new_r,new_c,k-1)
                else:
                    ans += 1
            return ans
        return dfs(sr,sc,maxMove)%(10**9 + 7)