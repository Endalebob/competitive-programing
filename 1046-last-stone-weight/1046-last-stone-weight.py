class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while stones:
            a = -1 * heapq.heappop(stones)
            if not stones:
                return a
            b = -1 * heapq.heappop(stones)
            if a>b:
                heapq.heappush(stones,b-a)
            if len(stones) == 1:
                return -1 * heapq.heappop(stones)
        return 0