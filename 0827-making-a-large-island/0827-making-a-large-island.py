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
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n*n)
        directions = [[0, 1], [1, 0]]
        isvalid = lambda r, c: 0 <= r < n and 0 <= c < n
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx,dy in directions:
                        r,c = dx+i,dy+j
                        if isvalid(r,c) and grid[r][c] == 1:
                            uf.union(r*n+c,i*n+j)
        directions = [[0, 1], [1, 0],[-1,0],[0,-1]]
        ans = uf.size(0)-1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    vstd = set()
                    temp = 0
                    for dx,dy in directions:
                        r,c = dx+i,dy+j
                        if isvalid(r,c) and grid[r][c] == 1:
                            find = uf.find(r*n+c)
                            if find not in vstd:
                                vstd.add(find)
                                temp += uf.size(find)
                    ans = max(ans,temp)
        return ans+1
                            
        
        
        
        
        
        
        
        