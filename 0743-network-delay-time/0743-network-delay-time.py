class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        all_node = [float('inf') for i in range(n+1)]
        all_node[0] = 0
        graph = defaultdict(list)
        for i,j,w in times:
            graph[i].append((j,w))
        all_node[k] = 0
        vstd = set()
        heap = []
        heapq.heappush(heap,(0,k))
        while len(vstd) < n and heap:
            w,node = heapq.heappop(heap)
            
            if node in vstd:
                continue
            
            vstd.add(node)
            for neigh, weight in graph[node]:
                if w + weight < all_node[neigh]:
                    all_node[neigh] = w + weight
                    heapq.heappush(heap,((w+weight,neigh)))
        ans= max(all_node)
        return ans if ans != inf else -1
            
                
            