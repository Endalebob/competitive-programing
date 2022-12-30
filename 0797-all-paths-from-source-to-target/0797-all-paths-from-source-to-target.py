class Solution:
    def allPathsSourceTarget(self, grap: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for i in range(len(grap)):
            for j in grap[i]:
                graph[i].append(j)
        ans = []
        def dp(node,path):
            path.append(node)
            if node == len(grap)-1:
                ans.append(deepcopy(path))
                path.pop()
                return
            for i in graph[node]:
                dp(i,path)
            path.pop()
        dp(0,[])
        return ans