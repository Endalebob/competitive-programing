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
            return 0

        if self.rank[ap] < self.rank[bp]:
            ap, bp = bp, ap
        self.parents[bp] = ap
        self.rank[ap] += self.rank[bp]

        return 1

    def size(self, x):
        return self.rank[self.find(x)]

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        uf = UnionFind(len(row))
        for i in range(0,len(row),2):
            uf.union(row[i],row[i+1])
        ans = 0
        for i in range(0,len(row),2):
            ans += uf.union(i,i+1)
        return ans
        