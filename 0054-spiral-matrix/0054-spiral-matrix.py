class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = [[0,1],[1,0],[0,-1],[-1,0]]
        m,n = len(matrix),len(matrix[0])
        isValid = lambda r,c:0<=r<m and 0<=c<n and matrix[r][c] != '7'
        
        ans = []
        r,c = 0,-1
        while len(ans) < m*n:
            for i,j in path:
                while isValid(r+i,c+j):
                    r += i
                    c += j
                    ans.append(matrix[r][c])
                    matrix[r][c] = '7'
        return ans