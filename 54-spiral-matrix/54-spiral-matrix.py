class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        r,c = 0,-1
        r_dir,c_dir = 0,1
        length = 0
        length_row,length_col = len(matrix[0]),len(matrix)-1
        for i in range(length_row*(length_col+1)):
            r += r_dir
            c += c_dir
            ans.append(matrix[r][c])
            length += 1
            if (r_dir != 0 and length == length_col) or (c_dir != 0 and length == length_row):
                if r_dir != 0:
                    length_col -= 1
                else:
                    length_row -= 1
                r_dir, c_dir = c_dir, -r_dir
                length = 0
        return ans