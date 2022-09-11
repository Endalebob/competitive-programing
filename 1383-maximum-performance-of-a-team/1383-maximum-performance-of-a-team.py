class Solution:
    def maxPerformance(self, n: int, sp: List[int], ef: List[int], k: int) -> int:
        zipped = sorted(zip(ef,sp),key = lambda i:-i[0])
        heap = []
        ans = 0
        tot = 0
        for i,j in zipped:
            tot += j
            heapq.heappush(heap,j)
            if len(heap)>k:
                tot -= heapq.heappop(heap)
            ans = max(ans,tot*i)
        return ans%(10**9+7)