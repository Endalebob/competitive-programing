class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i in range(1,len(parent)):
            graph[i].append(parent[i])
            graph[parent[i]].append(i)
        vstd = set()
        self.ans = 0
        def rec(r):
            left,right = 0,0
            vstd.add(r)
            for i in graph[r]:
                if i not in vstd:
                    temp = 1+rec(i)
                    if s[i] != s[r]:
                        left = max(left,temp)
                        if left>right:
                            left,right = right,left
            self.ans = max(self.ans,right+left)
            return right
        rec(0)
        return self.ans+1
                    