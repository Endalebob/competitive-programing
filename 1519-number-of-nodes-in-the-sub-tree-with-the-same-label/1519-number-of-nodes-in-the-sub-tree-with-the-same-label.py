class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        dp = {}
        ans = [1]*len(labels)
        vstd = set()
        vstd.add(0)
        def rec(idx):
            if idx not in graph:
                return {labels[idx]:1}
            if idx in dp:
                return dp[idx]
            val = defaultdict(int)
            val[labels[idx]] += 1
            for i in graph[idx]:
                if i not in vstd:
                    vstd.add(i)

                    temp = rec(i)
                    for j in temp:
                        val[j] += temp[j]
            dp[idx] = val
            ans[idx] = val[labels[idx]]
            return val
        rec(0)
        return ans
        
        