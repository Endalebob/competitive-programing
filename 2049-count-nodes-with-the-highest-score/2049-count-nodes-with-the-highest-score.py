class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        ret = [0]*n
        graph = defaultdict(set)
        for i in range(n):
            graph[parents[i]].add(i)
        def dfs(node):
            ans = 1
            rem = n-1
            for i in graph[node]:
                curr = dfs(i)
                rem -= curr
                ans *= curr
            ret[node] = max(1,rem)*ans
            return n-rem
        dfs(0)
        print(ret)
        return ret.count(max(ret))
            