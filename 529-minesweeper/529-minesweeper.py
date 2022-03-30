class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirction = [[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[-1,0]]
        row,col = len(board),len(board[0])
        isValid = lambda r,c: 0<=r<row and 0<=c<col  
        def dfs(r,c):
            if board[r][c] == "E":
                board[r][c] = 0
                for i in dirction:
                    new_row,new_col = r+i[0],c+i[1]
                    if isValid(new_row,new_col) and str(board[new_row][new_col]) == "M":
                        board[r][c] += 1
                if board[r][c] == 0:
                    board[r][c] = "B"
                    for i in dirction:
                        new_row,new_col = r+i[0],c+i[1]
                        if isValid(new_row,new_col):
                            dfs(new_row,new_col)
                else:
                    board[r][c] = str(board[r][c])

            elif board[r][c] == 'M':
                board[r][c] = "X"

        dfs(click[0],click[1])
        return board
                        