class UnionFind:
    def __init__(self,n,val):
        self.parents = [i for i in range(n)]
        self.max = [i for i in val]
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
        if self.max[ap] == self.max[bp]:
            self.parents[bp] = ap
            ans=self.rank[ap] * self.rank[bp]
            self.rank[ap] += self.rank[bp]
            return ans
        if self.max[ap] < self.max[bp]:
            self.parents[ap] = bp
        else:
            self.parents[bp] =  ap
        return 0
    
        
        
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        ans = len(vals)
        uf = UnionFind(ans,vals)
        edges.sort(key = lambda i: max(vals[i[0]],vals[i[1]]))
        
        for i,j in edges:
            ans += uf.union(i,j)
        return ans
        
        
        
        
        
        
        
        
        
        
    
    