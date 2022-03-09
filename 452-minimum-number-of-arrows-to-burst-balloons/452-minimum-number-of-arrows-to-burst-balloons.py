class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heapq.heapify(points)
        count = 1
        check = points[0]
        while points:
            a = heapq.heappop(points)
            if a[0]>check[1]:
                count += 1
                check = a
            if a[1]<check[1]:
                check[1] = a[1]
        return count