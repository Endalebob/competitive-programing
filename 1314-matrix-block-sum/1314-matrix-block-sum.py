class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        def calculate(r,c):
            ans = 0
            for i in range(max(0,r-k),min(len(mat),r+k+1)):
                for j in range(max(0,c-k),min(len(mat[0]),c+k+1)):
                    ans += mat[i][j]
                    
            return ans
        return [[calculate(r,c) for c in range(len(mat[0]))] for r in range(len(mat))]