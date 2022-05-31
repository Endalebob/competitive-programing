import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        idx = 0
        for i,v in edges:
            graph[i].append((v,succProb[idx]))
            graph[v].append((i,succProb[idx]))
            idx += 1
        vstd = set()
        heap =[]
        heapq.heappush(heap,[-1,start])
        while heap:
            val, node = heapq.heappop(heap)
            vstd.add(node)
            if node == end:
                return -val
            for nod,pro in graph[node]:
                if nod not in vstd:
                    a = val*pro
                    heapq.heappush(heap,[a,nod])
        return 0
            
        