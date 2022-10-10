class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        blue,red = defaultdict(list),defaultdict(list)
        for i,j in redEdges:
            red[i].append(j)
        for i,j in blueEdges:
            blue[i].append(j)
        def find(start,end,flag):
            deq = deque([[start,flag]])
            vstd = {(start,flag%2)}
            while deq:
                curr,flag = deq.popleft()
                if curr == end:
                    return flag
                if flag % 2 == 1:
                    for i in blue[curr]:
                        if (i,(flag+1)%2) not in vstd:
                            vstd.add((i,(flag+1)%2))
                            deq.append([i,flag+1])
                else:
                    for i in red[curr]:
                        if (i,(flag+1)%2) not in vstd:
                            vstd.add((i,(flag+1)%2))
                            deq.append([i,flag+1])
            return float('inf')
        
        ans = [-1]*n
        for i in range(n):
            re = find(0,i,0)
            bl = find(0,i,1)-1
            if re > 100000 and bl > 10000000:
                continue
            else:
                ans[i] = min(re,bl)
        return ans
        