class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points)<2:
            return 0
        graph = self.mk_graph(points)
        graph.sort(key = lambda x:x[2])
        Set = UnionFind(len(points))
        count = 1
        result = 0

        for i in graph:
            e1,e2,cost = i
            if count == len(points):
                return result
            if Set.union(e1,e2):
                result += cost
                count += 1
        return result

    def mk_graph(self,pts):
        graph = []
        for i in range(len(pts)-1):
            for j in range(i+1,len(pts)):
                val = abs(pts[i][0]-pts[j][0]) + abs(pts[i][1]-pts[j][1])
                graph.append([i,j,val])
        return graph
class UnionFind:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in self.root]
    def find(self, vertex):
        if vertex == self.root[vertex]:
            return vertex
        self.root[vertex] = self.find(self.root[vertex])
        return self.root[vertex]
    def union(self,e1,e2):
        node1 = self.find(e1)
        node2 = self.find(e2)
        if node1 != node2:
            if self.rank[node2]>self.rank[node1]:
                self.root[node1] = node2
            elif self.rank[node2]<self.rank[node1]:
                self.root[node2] = node1
            else:
                self.root[node2] = node1
                self.rank[node1] += 1
            return True
        return False