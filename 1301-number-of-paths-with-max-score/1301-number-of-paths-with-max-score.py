class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        row,col = len(board),len(board[0])
        isvalid = lambda r,c : 0<=r<row and 0<=c<col and board[r][c] != 'X'
        dirc = [[0,1],[1,0],[1,1]]
        @lru_cache(None)
        def dp(i,j):
            if i == row-1 and j == col-1:
                return [0,1]
            ans = [-float('inf'),0]
            for ir,ic in dirc:
                r,c = ir+i,ic+j
                if isvalid(r,c):
                    tempkey = dp(r,c)
                    if tempkey[0] > ans[0]:
                        ans = tempkey
                    elif tempkey[0] == ans[0]:
                        ans[1] += tempkey[1]
            if i+j > 0:
                return [ans[0]+int(board[i][j]),ans[1]]
            return ans
        val = dp(0,0)
        if val[0] < 0:
            return [0,0]
        return [val[0],val[1]%(10**9+7)]
                            
                