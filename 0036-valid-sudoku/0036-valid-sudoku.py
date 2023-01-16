class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        all_cand = {'1','2','3','4','5','6','7','8','9'}
        def get_candidate(r,c):
            not_include = set()
            for i in range(9):
                 if board[r][i] != '.':
                    if board[r][i] in not_include:
                        return False
                    not_include.add(board[r][i])
            not_include = set()
            for i in range(9):
                 if board[i][c] != '.':
                    if board[i][c] in not_include:
                        return False
                    not_include.add(board[i][c])
            start_r,start_c = (r//3) * 3,(c//3)*3
            not_include = set()
            for i in range(3):
                  for j in range(3):
                    if board[start_r+i][start_c+j] != '.':
                        if board[start_r+i][start_c+j] in not_include:
                            return False
                        not_include.add(board[start_r+i][start_c+j])
            return True
        for r in range(9):
            for c in range(9):
                if not get_candidate(r,c):
                    return False
        return True