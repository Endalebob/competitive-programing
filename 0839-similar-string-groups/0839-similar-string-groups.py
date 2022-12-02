class UnionFind:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.group = n
    def find(self,xp):
        comp = []
        while xp != self.parents[xp]:
            comp.append(xp)
            xp = self.parents[xp]
        for i in comp:
            self.parents[i] = xp
        return xp
    def union(self,a,b):
        ap,bp = self.find(a),self.find(b)
        if ap == bp:
            return
        if self.rank[bp] > self.rank[ap]:
            ap,bp = bp,ap
        self.parents[bp] = ap
        self.rank[ap] += self.rank[bp]
        self.group -= 1
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        strs = list(set(strs))
        uf = UnionFind(len(strs))
        def check(i,j):
            dif = []
            for ii in range(len(strs[i])):
                if strs[i][ii] != strs[j][ii]:
                    dif.append(ii)
                    if len(dif) > 2:
                        return
            if len(dif) == 2 and strs[i][dif[0]] == strs[j][dif[1]] and strs[j][dif[0]] == strs[i][dif[1]]:
                uf.union(i,j)
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if uf.find(i) != uf.find(j):
                    check(i,j)
        return uf.group  
        