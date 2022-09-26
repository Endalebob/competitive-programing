class DSU:
    def __init__(self,nodes):
        self.root = [i for i in range(nodes)]
        self.rank = [1 for i in range(nodes)]
    def find(self,node):
        while node != self.root[node]:
            node = self.root[node]
        return node
    def union(self,node1,node2):
        a,b = self.find(node1),self.find(node2)
        if a == b:
            return False
        if self.rank[a]<self.rank[b]:
            a,b = b,a
        self.rank[a] += 1
        self.root[b] = a
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = sorted((w, u, v, i) for i, (u, v, w) in enumerate(edges))
        critical, pseudo = [], []
        for _w, _u, _v, i in edges:
            dsu1, dsu2 = DSU(n), DSU(n)
            dsu1.union(_u, _v)
            s1, s2 = _w, 0
            for w, u, v, j in edges:
                if i == j:
                    continue
                if dsu1.union(u, v):
                    s1 += w
                if dsu2.union(u, v):
                    s2 += w
            if s1 == s2:
                pseudo.append(i)
            elif s1 < s2 or dsu2.union(_u, _v):
                critical.append(i)
        return critical, pseudo