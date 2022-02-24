class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        one_dimensional = []
        for i in matrix:
            for j in i:
                heapq.heappush(one_dimensional,j)
        for i in range(k-1):
            heapq.heappop(one_dimensional)
        return heapq.heappop(one_dimensional)