class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        ans = []
        vstd = set()
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                graph[accounts[i][j]].append(i)
        relation = list(graph.values())
        print(relation)
        sub_set = UnionFind(len(accounts))
        for i in range(len(relation)):
            for j in range(1,len(relation[i])):
                accounts = sub_set.union(relation[i][0],relation[i][j],accounts)
        lenght = len(accounts)
        i = 0
        while i<len(accounts):            
            index = sub_set.find(i)
            if index not in vstd and index == i:
                sort = set(accounts[index][1:])
                sort = list(sort)
                sort.sort()
                temp = [accounts[index][0]]
                temp.extend(sort)
                ans.append(temp)
                vstd.add(index)
            i += 1
        return ans
                
        
        
        
class UnionFind:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in self.root]
    def find(self, vertex):
        if vertex == self.root[vertex]:
            return vertex
        self.root[vertex] = self.find(self.root[vertex])
        return self.root[vertex]
    def union(self,e1,e2,acc):
        node1 = self.find(e1)
        node2 = self.find(e2)
        if node1 != node2:
            if self.rank[node2]>self.rank[node1]:
                acc[node2].extend(acc[node1][1:])
                self.root[node1] = node2
            elif self.rank[node2]<self.rank[node1]:
                acc[node1].extend(acc[node2][1:])
                self.root[node2] = node1
            else:
                acc[node1].extend(acc[node2][1:])
                self.root[node2] = node1
                self.rank[node1] += 1
        return acc
                    