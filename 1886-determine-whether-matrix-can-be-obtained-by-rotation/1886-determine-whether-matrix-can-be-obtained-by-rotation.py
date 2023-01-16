class Solution:
    def findRotation(self, matrix: List[List[int]], target: List[List[int]]) -> bool:
        def rotator(n):
            for i in range(n):
                for j in range(i,n):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            for i in range(n):
                for j in range(n//2):
                    matrix[i][j],matrix[i][-1-j] = matrix[i][-1-j],matrix[i][j]
            return matrix
        for i in range(4):
            if rotator(len(matrix)) == target:
                return True
        return False