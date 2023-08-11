class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio_list = [(wage[i]/quality[i],quality[i],wage[i]) for i in range(len(wage))]
        ratio_list.sort()
        
        ans = float('inf')
        curr = 0
        heap = []
        for r,q,w in ratio_list:
            curr += q
            heapq.heappush(heap,-q)
            
            if len(heap) > k:
                curr += heapq.heappop(heap)
            if len(heap) == k:
                ans = min(ans,curr*r)
        return ans