class UnionFind:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
    def find(self,xp):
        compress = []
        while xp != self.parents[xp]:
            compress.append(xp)
            xp = self.parents[xp]
        for i in compress:
            self.parents[i] = xp
        return xp
    
    def union(self,a,b):
        ap,bp = self.find(a),self.find(b)
        if ap == bp:
            return 0
        if self.rank[ap] < self.rank[bp]:
            ap,bp = bp,ap
        self.rank[ap] += self.rank[bp]
        self.parents[bp] = ap
        return 1
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(len(stones))
        removed = 0
        rows,cols = {},{}
        for i in range(len(stones)):
            row,col = stones[i]
            if row in rows:
                removed += uf.union(i,rows[row])
            else:
                rows[row] = i
            if col in cols:
                removed += uf.union(i,cols[col])
            else:
                cols[col] = i
        return removed