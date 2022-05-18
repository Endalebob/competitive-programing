class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for i,v in connections:
            dic[i].append(v)
            dic[v].append(i)
        ans = []
        disc = [-1] * n
        low = [-1] * n
        self.time = 0
        def dfs(node,parent):
            if disc[node] != -1:
                return
            disc[node] = self.time
            low[node] = self.time
            self.time += 1
            for i in dic[node]:
                if i != parent:
                    dfs(i,node)
                    low[node] = min(low[i],low[node])
                    if disc[node] < low[i]:
                        ans.append([node,i])
        dfs(0,-8)
        return ans