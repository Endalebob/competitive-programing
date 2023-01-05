class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        curr,ans = points[0][1],1
        i = 1
        while i<len(points):
            if curr >= points[i][0]:
                curr = min(curr,points[i][1])
            else:
                ans += 1
                curr = points[i][1]
            i += 1
        return ans