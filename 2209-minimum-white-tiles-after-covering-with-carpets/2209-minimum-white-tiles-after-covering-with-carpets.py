class Solution:
    def minimumWhiteTiles(self, floor: str, nc: int, cl: int) -> int:
        pre_sum = [0 for i in range(len(floor)+1)]
        j = len(floor)-1
        while j>=0:
            pre_sum[j] = pre_sum[j+1]
            if floor[j] == '1':
                pre_sum[j] += 1
            j-=1
        @lru_cache(None)
        def rec(i,j):
            if i >= len(floor):
                return 0
            if j == 0:
                return pre_sum[i]
            if j*cl+i >= len(floor):
                return 0
            if floor[i] == '1':
                return min(rec(i+cl,j-1),rec(i+1,j)+1)
            return rec(i+1,j)
        return rec(0,nc)
            
            