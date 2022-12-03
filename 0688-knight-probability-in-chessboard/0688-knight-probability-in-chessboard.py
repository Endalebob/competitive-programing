class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        move = [[[1,1],[-1]],[[1,1],[1]],[[-1,-1],[-1]],[[-1,-1],[1]],[[1],[1,1]],[[-1],[1,1]],[[1],[-1,-1]],[[-1],[-1,-1]]]
        is_valid = lambda r,c : 0<=r<n and 0<=c<n
        @lru_cache(None)
        def dfs(r,c,k):
            if k == 0:
                return 1
            ans = 0
            for d in move:
                new_r,new_c = r,c
                i,j = d[0],d[1]
                for kk in i:
                    new_r += kk
                for kk in j:
                    new_c += kk
                if is_valid(new_r,new_c):
                    ans += dfs(new_r,new_c,k-1)/8
            return ans
        return dfs(row,column,k)
            