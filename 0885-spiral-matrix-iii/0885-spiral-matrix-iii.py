class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        matrix = [[0 for col in range(cols)] for row in range(rows)]
        isvalid = lambda r,c : 0<=r<rows and 0<=c<cols and matrix[r][c] == 0 
        
        matrix[rStart][cStart] = 1
        ans = [[rStart,cStart]]
        k = 1
        
        while len(ans) != rows*cols:
            for dr,dc in [[0,1],[1,0]]:
                for _ in range(k):
                    rStart += dr
                    cStart += dc
                    if isvalid(rStart,cStart):
                        ans.append([rStart,cStart])
                        matrix[rStart][cStart] = 1
            k += 1
            for dr,dc in [[0,-1],[-1,0]]:
                for _ in range(k):
                    rStart += dr
                    cStart += dc
                    
                    if isvalid(rStart,cStart):
                        ans.append([rStart,cStart])
                        matrix[rStart][cStart] = 1
            k += 1
        return ans