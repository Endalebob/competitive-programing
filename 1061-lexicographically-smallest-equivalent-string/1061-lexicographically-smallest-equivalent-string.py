class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dic = defaultdict(set)
        for i,j in zip(s1,s2):
            dic[i].add(j)
            dic[j].add(i)
        ans = ''
        
        def dfs(node):
            if node in vstd:
                return node
            vstd.add(node)
            ans = node
            for i in dic[node]:
                ans = min(dfs(i),ans)
            return ans
        for i in baseStr:
            vstd = set()
            ans += dfs(i)
        return ans
            