class UnionFind:
    def __init__(self):
        self.root = [i for i in range(26)]
        self.rank = [1 for _ in range(26)]
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
    def equationsPossible(self, equations: List[str]) -> bool:
        equ,n_eq = '==','!='
        uf = UnionFind()
        for i in equations:
            a,b = ord(i[0])-ord('a'),ord(i[-1])-ord('a')
            if i[1:-1] == equ:
                if uf.find(a) != uf.find(b):
                    uf.union(a,b)
                    
        for i in equations:
            a,b = ord(i[0])-ord('a'),ord(i[-1])-ord('a')
            if i[1:-1] == n_eq:
                if uf.find(a) == uf.find(b):
                    return False
        return True