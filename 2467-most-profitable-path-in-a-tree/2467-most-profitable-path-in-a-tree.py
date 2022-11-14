class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        self.ans = -float('inf')
        vstd = set()
        vs = set()
        def path(node,pa):
            vs.add(node)
            if node == 0:
                return pa,True
            for i in graph[node]:
                if i not in vs:
                    pa.append(i)
                    temp = path(i,pa)
                    if temp[1]:
                        return temp
                    pa.pop()
            return pa,False
        pat = path(bob,[bob])[0]
        if len(pat) % 2:
            for i in range(len(pat)//2):
                amount[pat[i]] = 0
            amount[pat[len(pat)//2]] //= 2
        else:
            for i in range(len(pat)//2):
                amount[pat[i]] = 0
        def dfs(node,tot):
            vstd.add(node)
            if len(graph[node]) == 1 and node != 0:
                self.ans = max(self.ans,tot)
                return
            for i in graph[node]:
                if i not in vstd:
                    dfs(i,tot+amount[i])
        dfs(0,amount[0])
        return self.ans
            
        