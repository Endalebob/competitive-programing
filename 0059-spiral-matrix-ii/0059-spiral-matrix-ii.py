class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for col in range(n)] for row in range(n)]
        directions = [[0,1],[-1,0],[0,-1],[1,0]]
        isvalid = lambda r,c : 0<=r<n and 0<=c<n and matrix[r][c] == 0 
        matrix[0][0] = 1
        r,c = 0,0
        n_squer = n*n-1
        
        while n_squer:
            for dr,dc in directions:
                while isvalid(r+dr,c+dc):
                    r += dr
                    c += dc
                    matrix[r][c] = matrix[r-dr][c-dc]+1
                    n_squer -= 1
        return matrix
                
        