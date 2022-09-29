class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in arr:
            heapq.heappush(heap,(abs(x-i),i))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return sorted(ans)