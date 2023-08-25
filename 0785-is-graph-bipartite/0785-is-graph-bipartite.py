class Solution:
    def isBipartite(self, graphh: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for i in range(len(graphh)):
            for j in graphh[i]:
                graph[i].add(j)
        color = [-1]*len(graphh)
        def dfs(idx,col):
            if color[idx] != -1:
                return color[idx] == col
            color[idx] = col
            for i in graph[idx]:
                if not dfs(i,1-col):
                    return False
            return True
        for i in range(len(graphh)):
            if color[i] == -1:
                if not dfs(i,1):
                    return False
        return True
                
                