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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        dic = defaultdict(set)
        ans = [True]*len(requests)
        for k in range(len(requests)):
            flag = True
            a,b = requests[k]
            ap,bp = uf.find(a),uf.find(b)
            for i,j in restrictions:
                pi,pj = uf.find(i),uf.find(j)
                
                if set([ap,bp]) == set([pi,pj]):
                    flag = False
                    break
            if flag:
                uf.union(requests[k][0],requests[k][1])
            ans[k] = flag
        return ans
        

        
        
        