import heapq
import sys, threading

from collections import defaultdict
class UnionFind:
    def __init__(self, n,m):
        self.parents = {}
        self.rank = {}
        for i in range(n):
            for j in range(m):
                self.parents[(i,j)] = (i,j)
                self.rank[(i,j)] = 1
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


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n,n)
        directions = [[0, 1], [1, 0],[-1,0],[0,-1]]
        isvalid = lambda r, c: 0 <= r < n and 0 <= c < n and grid[r][c] == 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx,dy in directions:
                        r,c = dx+i,dy+j
                        if isvalid(r,c):
                            uf.union((i,j),(r,c))
        ans = uf.rank[uf.find((0,0))]-1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    temp = 0
                    vstd = set()
                    for dx,dy in directions:
                        r,c = dx+i,dy+j
                        if isvalid(r,c):
                            val = uf.find((r,c))
                            if val not in vstd:
                                vstd.add(val)
                                temp += uf.rank[val]
                    ans = max(ans,temp)
        return ans+1
        
        
        
        
        
        
        
        