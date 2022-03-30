class Solution:
    def minn(self,grid,r,c,dic):
        if r == len(grid)-1 and c == len(grid[0])-1:
            return grid[r][c]
        if r>=len(grid) or c>=len(grid[0]):
            return 1000000
        if (r,c) in dic: return dic[(r,c)]
        dic[r,c] = grid[r][c] + min(self.minn(grid,r,c+1,dic),self.minn(grid,r+1,c,dic))
        return dic[(r,c)]
    def minPathSum(self, grid: List[List[int]]) -> int:
        dic = {}
        return self.minn(grid,0,0,dic)