class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotator(n):
            for i in range(n):
                for j in range(i,n):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            for i in range(n):
                for j in range(n//2):
                    matrix[i][j],matrix[i][-1-j] = matrix[i][-1-j],matrix[i][j]
        rotator(len(matrix))