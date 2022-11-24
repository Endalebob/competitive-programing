class UnionFind:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
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
        
        if self.rank[ap] < self.rank[bp]:
            ap,bp = bp,ap
        self.parents[bp] = ap
        self.rank[ap] += self.rank[bp]
class Solution:
    
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def is_in_range(x1,y1,x2,y2,r):
            x_squere = (x1-x2) ** 2
            y_squere = (y1-y2) ** 2
            
            return r**2 >= x_squere + y_squere
        ret = 1
        graph = defaultdict(list)
        uf = UnionFind(len(bombs))
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if is_in_range(bombs[i][0],bombs[i][1],bombs[j][0],bombs[j][1],bombs[i][2]):
                    graph[i].append(j)
                    
        def dfs(node):
            vstd.add(node)
            ans = 1
            for i in graph[node]:
                if i not in vstd:
                    ans += dfs(i)
            return ans
        ret = 1
        for i in range(len(bombs)):
            vstd = set()
            ret = max(dfs(i),ret)
        return ret