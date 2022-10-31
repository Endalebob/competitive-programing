class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.num_dis_set = n

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

        self.num_dis_set -= 1

    def size(self, x):
        return self.rank[self.find(x)]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 1
        for i,j in edges:
            n = max(n,i,j)
        uf = UnionFind(n)
        
        ans = []
        for i,j in edges:
            if uf.find(i-1) == uf.find(j-1):
                ans = [i,j]
            else:
                uf.union(i-1,j-1)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        