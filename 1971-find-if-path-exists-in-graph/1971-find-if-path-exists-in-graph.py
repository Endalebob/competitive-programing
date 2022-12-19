class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, d: int) -> bool:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        vstd = set()
        def dfs(node,target):
            if node == target:
                return True
            if node in vstd:
                return False
            vstd.add(node)
            for i in graph[node]:
                if dfs(i,target):
                    return True
            return False
        return dfs(source,d)
            
        