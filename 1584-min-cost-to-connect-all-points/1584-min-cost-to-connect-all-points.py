class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dis = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(heap,[dis,(i,j)])
        ans = 0
        UF = UnionFind(len(points))
        while heap:
            curr = heapq.heappop(heap)
            a = UF.find(curr[1][0])
            if a == UF.find(curr[1][1]):
                if UF.rank[a] == len(points):
                    break
                continue
            ans += curr[0]
            UF.union(curr[1][0],curr[1][1])
        return ans
    
class UnionFind:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    def union(self,aa,bb):
        a = self.find(aa)
        b = self.find(bb)
        if self.rank[a]<self.rank[b]:
            a,b = b,a
        self.rank[a] += self.rank[b]
        self.root[b] = a