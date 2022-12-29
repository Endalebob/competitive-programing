class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        p_time = defaultdict(list)
        for i,j in enumerate(tasks):
            p_time[j[0]].append([j[1],i])
        keys = sorted(p_time.keys())
        idx = 1
        heap = p_time[keys[0]]
        heapq.heapify(heap)
        tot = keys[0]
        ans = []
        while heap:
            ad,i = heapq.heappop(heap)
            ans.append(i)
            tot += ad
            while idx<len(keys) and tot >= keys[idx]:
                for k in p_time[keys[idx]]:
                    heapq.heappush(heap,k)
                idx += 1
            if idx < len(keys) and not heap:
                for k in p_time[keys[idx]]:
                    heapq.heappush(heap,k)
                idx += 1
                tot = keys[idx-1]
        return ans