class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirc = [[0,1],[1,0],[-1,0],[0,-1]]
        is_valid = lambda r,c:0<=r<len(board) and 0<=c<len(board[0])
        def dfs(m,n,le):
            temp = board[m][n]
            board[m][n] = '#'
            if le == len(word):
                return True
            for i,j in dirc:
                new_m,new_n = i+m,j+n
                if is_valid(new_m,new_n) and board[new_m][new_n] == word[le]:
                    if dfs(new_m,new_n,le+1):
                        return True
            board[m][n] = temp  
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,1):
                        return True
        return False