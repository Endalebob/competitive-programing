class UnionFind:
    def __init__(self, nums):
        self.root = {}
        self.rank = {}
        self.ans = 0
        if nums:
            self.ans = 1
        for i in nums:
            self.root[i] = i
            self.rank[i] = 1

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, aa, bb):
        a, b = self.find(aa), self.find(bb)
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.rank[a] += self.rank[b]
        self.root[b] = a
        self.ans = max(self.ans, self.rank[a])


class Solution:
    def longestConsecutive(self, nums) -> int:
        uf = UnionFind(nums)
        nums = set(nums)
        for i in nums:
            if i - 1 in nums:
                uf.union(i - 1, i)
        return uf.ans
