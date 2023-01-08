class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''
        slope = y2-y1/(x2-x1)
        '''
        ans = 0
        for i in range(len(points)-ans):
            dic = defaultdict(int)
            for j in range(i+1,len(points)):
                if points[i][0] - points[j][0] == 0:
                    slope = 11111111111
                else:
                    slope = (points[i][1] - points[j][1])/(points[i][0]-points[j][0])
                dic[slope] += 1
                ans = max(ans,dic[slope])
        return ans+1
        