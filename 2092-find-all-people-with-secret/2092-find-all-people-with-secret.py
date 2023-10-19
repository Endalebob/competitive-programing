class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    def find(self,a):
        compress = []
        while a != self.parent[a]:
            compress.append(a)
            a = self.parent[a]
        for i in compress:
            self.parent[i] = a
        return a
            
    def union(self,a,b):
        ap,bp = self.find(a),self.find(b)
        if ap == bp:
            return
        if self.rank[ap] < self.rank[bp]:
            ap,bp = bp,ap
        self.parent[bp] = ap
        self.rank[ap] += 1
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        uf = UnionFind(n)
        uf.union(0,firstPerson)
        
        time = defaultdict(list)
        for a,b,t in meetings:
            time[t].append((a,b))
        keys = sorted(time.keys())
        z_p = uf.find(0)
        for i in keys:
            for j,k in time[i]:
                uf.union(j,k)
            for j,k in time[i]:
                if uf.find(j) != uf.find(0) or uf.find(k) != uf.find(0):
                    uf.parent[j] = j
                    uf.parent[k] = k
        return [i for i in range(n) if uf.find(i) == uf.find(0)]
        