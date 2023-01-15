class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        linear --> to grid
        linear = arr[n] --> grid[n//m][n%m]
        '''
        n,m = len(matrix),len(matrix[0])
        
        def convertor(n):
            return n//m,n%m
        
        l,r = 0,m*n-1
        while l <= r:
            mid = l + (r-l)//2
            rr,c = convertor(mid)
            if matrix[rr][c] == target:
                return True
            elif matrix[rr][c] > target:
                r = mid-1
            else:
                l = mid+1
        return False
            