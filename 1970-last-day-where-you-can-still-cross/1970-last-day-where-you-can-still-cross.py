class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
 
    def find(self, xp):
        compress = []
        while xp != self.parents[xp]:
            compress.append(xp)
            xp = self.parents[xp]
 
        for i in compress:
            self.parents[i] = xp
 
        return xp
 
    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
 
        if ap == bp:
            return
 
        if self.rank[ap] < self.rank[bp]:
            ap, bp = bp, ap
        self.parents[bp] = ap
        self.rank[ap] += self.rank[bp]
        
        
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        uf = UnionFind(row*col+20)
        current = [[1 for i in range(col)] for j in range(row)]
        dirc = ((0,1),(1,0),(-1,0),(0,-1))
        isvalid = lambda r,c: 0<=r<row and 0<=c<col and current[r][c] == 0
        for i in range(len(cells)):
            r,c = cells[-i-1][0]-1,cells[-i-1][1]-1
            current[r][c] = 0
            one_idx = r*col+c+1
            for dr,dc in dirc:
                new_r,new_c = r+dr,c+dc
                one_idx2 = new_r*col+new_c+1
                if isvalid(new_r,new_c):
                    uf.union(one_idx,one_idx2)
            if r == 0:
                uf.union(0,one_idx)
            if r == row-1:
                uf.union(row * col + 1,one_idx)
            if uf.find(0) == uf.find(row * col + 1):
                return row*col-i-1