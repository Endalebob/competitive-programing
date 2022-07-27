class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.pre_sum = []
        a=0
        for i in range(len(matrix)):
            lis = []
            for j in range(len(matrix[0])):
                lis.append(a+matrix[i][j])
                a+=matrix[i][j]
            self.pre_sum.append(lis)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row2-row1+1):
            add = self.pre_sum[row1+i][col2]-self.pre_sum[row1+i][col1]+self.matrix[row1+i][col1]
            ans += add
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)