class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x
        def union(a,b):
            ap,bp = find(a),find(b)
            if ap == bp:
                return False
            parent[bp] = ap
            return True
        vstd = [0]*(len(edges)+1)
        flag = False
        for i,j in edges:
            if vstd[j]:
                flag = True
                node,p1,p2 = j,vstd[j],i
            vstd[j] = i
        
        if not flag:
            for i,j in edges:
                if not union(i,j):
                    return [i,j]
        edges.remove([p2,node])
        for i,j in edges:
            if not union(i,j):
                return [p1,node]
        return [p2,node]
        
                