class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        node_count,ans = [1]*n,[0]*n
        def dfs(node,par):
            for i in graph[node]:
                if i != par:
                    dfs(i,node)
                    node_count[node] += node_count[i]
                    ans[node] += ans[i] + node_count[i]
        def dfs2(node,par):
            for i in graph[node]:
                if i != par:
                    ans[i] = ans[node] - node_count[i] + n-node_count[i]
                    dfs2(i,node)
        dfs(0,-1)
        dfs2(0,-1)
        return ans
        