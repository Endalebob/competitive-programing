class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        first I build the graph.
        then I start from the k node and go until all nodes receive the mesage if it is possible.
        
        use bfs
        '''
        graph = defaultdict(list)
        for i,j,w in times:
            graph[i].append([j,w])
        
        
        heap = [[0,k]]
        heapq.heapify(heap)
        vstd = {k}
        while heap:
            w,node = heapq.heappop(heap)
            vstd.add(node)
            if len(vstd) == n:
                return w
            for i in graph[node]:
                if i[0] not in vstd:
                    heapq.heappush(heap,[w+i[1],i[0]])
        return -1
            