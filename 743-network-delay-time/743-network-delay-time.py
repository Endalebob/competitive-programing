class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for i in times:
            graph[i[0]].append([i[2],i[1]])
        deq = graph[k]
        heapq.heapify(deq)
        vstd = {k}
        ans = 0
        while deq:
            curr = heapq.heappop(deq)
            vstd.add(curr[1])
            ans = max(ans,curr[0])
            if len(vstd) == n:
                return ans
            for i in graph[curr[1]]:
                if i[1] not in vstd:
                    c = i[0]+curr[0]
                    heapq.heappush(deq,[c,i[1]])
        return -1