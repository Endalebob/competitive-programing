class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        row,col = len(board),len(board[0])
        isvalid = lambda r,c : 0<=r<row and 0<=c<col and board[r][c] != 'X'
        dirc = [[0,1],[1,0],[1,1]]
        @lru_cache(None)
        def dp(i,j):
            if i == row-1 and j == col-1:
                return {0:1}
            ans = {-float('inf'):0}
            for ir,ic in dirc:
                r,c = ir+i,ic+j
                if isvalid(r,c):
                    temp = dp(r,c)
                    tempkey = list(temp.keys())
                    anskey = list(ans.keys())
                    if tempkey[0] > anskey[0]:
                        ans = {tempkey[0]:temp[tempkey[0]]}
                    elif tempkey[0] == anskey[0]:
                        ans[anskey[0]] += temp[tempkey[0]]
            anskey = list(ans.keys())
            if i+j > 0:
                return {anskey[0]+int(board[i][j]):ans[anskey[0]]}
            return ans
        val = dp(0,0)
        m = list(val.keys())
        if m[0] < 0:
            return [0,0]
        return [m[0],val[m[0]]%(10**9+7)]
                            
                