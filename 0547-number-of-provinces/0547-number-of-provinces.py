class UnionFind:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.size = n
        self.rank = [1]*n
        
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
            return
        if self.rank[bp] > self.rank[ap]:
            ap,bp = bp,ap
        self.rank[ap] += self.rank[bp]
        self.parents[bp] = ap
        self.size -= 1
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i,j)
        return uf.size
        