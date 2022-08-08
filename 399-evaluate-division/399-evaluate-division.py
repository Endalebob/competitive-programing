class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(values)):
            graph[equations[i][0]].append([equations[i][1],values[i]])
            graph[equations[i][1]].append([equations[i][0],1/values[i]])
        def bfs(start,end):
            vstd = set()
            vstd.add(start)
            deq = deque()
            deq.append([start,1])
            while deq:
                curr = deq.popleft()
                if curr[0] == end:
                    return curr[1]
                for i in graph[curr[0]]:
                    if i[0] not in vstd:
                        vstd.add(i[0])
                        temp = i[1]*curr[1]
                        deq.append([i[0],temp])
            return -1
        ans = []
        for i,j in queries:
            if i not in graph or j not in graph:
                ans.append(-1)
                continue
            ans.append(bfs(i,j))
        return ans
                