class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        check = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j in check:
                    if matrix[i][j] != check[i-j]:
                        return False
                else:
                    check[i-j] = matrix[i][j]
        return True