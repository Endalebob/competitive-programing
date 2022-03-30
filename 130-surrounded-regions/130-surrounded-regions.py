class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j,r,c):
            not_include.append([i,j])
            if j+1<c and board[i][j+1] == "O" and [i,j+1] not in not_include:
                dfs(i,j+1,r,c)
            if j-1>=0 and board[i][j-1] == "O" and [i,j-1] not in not_include:
                dfs(i,j-1,r,c)
            if i+1<r and board[i+1][j] == "O" and [i+1,j] not in not_include:
                dfs(i+1,j,r,c)
            if i-1>=0 and board[i-1][j] == "O" and [i-1,j] not in not_include:
                dfs(i-1,j,r,c)
                
        r = len(board)
        c = len(board[0])
        not_include = []
        for i in range(r):
            if board[i][0] == "O":
                dfs(i,0,r,c)
        for i in range(r):
            if board[i][c-1] == "O":
                dfs(i,c-1,r,c)
        for i in range(1,c-1):
            if board[0][i] == "O":
                dfs(0,i,r,c)
        for i in range(1,c-1):
            if board[r-1][i] == "O":
                dfs(r-1,i,r,c)
        for i in range(r):
            for j in range(c):
                if [i,j] not in not_include:
                    board[i][j] = "X"
        