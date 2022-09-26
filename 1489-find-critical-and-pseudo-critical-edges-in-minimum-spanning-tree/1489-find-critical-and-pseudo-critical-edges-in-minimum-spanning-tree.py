class UnionFind:
    def __init__(self,nodes):
        self.root = [i for i in range(nodes)]
        self.rank = [1 for i in range(nodes)]
    def find(self,node):
        while node != self.root[node]:
            node = self.root[node]
        return node
    def union(self,node1,node2):
        a,b = self.find(node1),self.find(node2)
        if self.rank[a]<self.rank[b]:
            a,b = b,a
        self.rank[a] += 1
        self.root[b] = a
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        critical, pseudo = [], []
        dic = {}
        for i, v in enumerate(edges):
            dic[tuple(v)] = i
        
        def kruskal():
            edge = sorted([w, u, v, i] for i, (u, v, w) in enumerate(edges))
            uf = UnionFind(n)
            cost = 0
            for i in edge:
                a,b = uf.find(i[1]),uf.find(i[2])
                if a != b:
                    uf.union(a,b)
                    cost += i[0]
            return cost
        mnv = kruskal()
        for i in range(len(edges)):
            temp = edges[i][2]
            edges[i][2] += 1
            d = kruskal()
            if mnv < d:
                edges[i][2] -= 1
                critical.append(dic[tuple(edges[i])])
            elif d == mnv:
                edges[i][2] -= 2
                if mnv > kruskal():
                    edges[i][2] += 1
                    pseudo.append(dic[tuple(edges[i])])
            edges[i][2] = temp
        return critical,pseudo
                
            