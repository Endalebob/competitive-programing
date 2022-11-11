class Solution:
    def allPathsSourceTarget(self, g: List[List[int]]) -> List[List[int]]:
        paths = []
        graph = defaultdict(list)
        target = 0
        for i in range(len(g)):
            for j in g[i]:
                target = max(target,j)
                graph[i].append(j)
        def dfs(node,path):
            if node == target:
                paths.append(deepcopy(path))
            for i in graph[node]:
                dfs(i,path+[i])
        dfs(0,[0])
        return paths