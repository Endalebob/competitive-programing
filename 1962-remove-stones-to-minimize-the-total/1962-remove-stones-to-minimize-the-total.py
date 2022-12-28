class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
        heapq.heapify(piles)
        while k:
            curr = heapq.heappop(piles)
            curr -= int(curr/2)
            heapq.heappush(piles,curr)
            k -= 1
        return -sum(piles)
        