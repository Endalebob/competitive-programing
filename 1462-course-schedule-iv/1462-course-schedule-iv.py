class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = []
        graph = defaultdict(list)
        for i,j in prerequisites:
            graph[i].append(j)
        glb = set()
        @lru_cache(None)
        def dfs(node,target):
            if node == target:
                return True
            for i in graph[node]:
                if dfs(i,target):
                    return True
            return False
                
        key = list(graph.keys())
        ret = []
        for i,j in queries:
            ret.append(dfs(i,j))
        return ret
                
        
            