class Solution:
    def find(self,a):
        if a != self.root[a]:
            self.root[a] = self.find(self.root[a])
        return self.root[a]
    def union(self,a,b):
        self.root[self.find(b)] = self.find(a)
    def isConnected(self,a,b):
        return self.find(a) == self.find(b)
    def findAllPeople(self, n: int, m: List[List[int]], f: int) -> List[int]:
        self.root = [i for i in range(n)]
        self.union(0,f)
        dic = defaultdict(list)
        for i in m:
            dic[i[2]].append(i[:2])
        for i in sorted(dic.keys()):
            vstd = set()
            for a,b in dic[i]:
                self.union(a,b)
                vstd.update({a,b})
            for j in vstd:
                if not self.isConnected(0,j):
                    self.root[j] = j
        return [i for i in range(n) if self.isConnected(0,i)]  