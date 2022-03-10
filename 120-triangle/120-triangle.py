class Solution:
    def minn(self,tri,dic,r,c):
        if r>=len(tri):
            return 0
        if (r,c) in dic: return dic[(r,c)]
        else:
            dic[(r,c)] =tri[r][c] + min(self.minn(tri,dic,r+1,c),self.minn(tri,dic,r+1,c+1))
            return dic[(r,c)]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dic = {}
        return self.minn(triangle,dic,0,0)