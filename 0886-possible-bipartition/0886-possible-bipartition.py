class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        group = {0:set(),1:set()}
        graph = defaultdict(set)
        for i,j in dislikes:
            graph[i].add(j)
            graph[j].add(i)
        vstd = set()
        def dfs(node,g):
            if node in vstd:
                return node not in group[1-g]
            group[g].add(node)
            vstd.add(node)
            for i in graph[node]:
                if not dfs(i,1-g):
                    return False
            return True
        for i in range(1,n+1):
            if i not in vstd:
                if not dfs(i,0):
                    return False
        return True