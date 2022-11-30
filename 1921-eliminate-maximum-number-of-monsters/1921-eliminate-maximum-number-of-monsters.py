class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i in range(len(dist)):
            dist[i] /= speed[i]
        heapq.heapify(dist)
        count = 0
        while dist:
            curr = heapq.heappop(dist)
            if curr > count:
                count += 1
            else:
                return count
        return count