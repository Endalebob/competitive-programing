class UnionFind:
    def __init__(self, nums):
        n = len(nums)
        self.parents = {i:i for i in nums}
        self.rank = {i:1 for i in nums}
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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        k = len(nums)
        setn = set(nums)
        nums = list(setn)
        nums.sort()
        if (len(nums) == 1 and nums[0] != 1) or k == 1:
            return True
        if 1 in setn:
            return False
        uf = UnionFind(nums)
        vstd = set()
        for i in range(2,nums[-1]//2 + 1):
            if i in vstd:
                continue
            flag = 0
            c = 2
            for k in range(i,nums[-1]+1,i):
                if k in setn:
                    if flag:
                        uf.union(k,flag)
                        if uf.size(k) == len(setn):
                            return True
                    else:
                        flag = k
                vstd.add(k)
                    
                
        return False
            
            