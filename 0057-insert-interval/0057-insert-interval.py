class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l,r = 0,len(intervals)
        m = 0
        while l<r:
            m = l+(r-l)//2
            if newInterval[0] >= intervals[m][0]:
                l = m+1
            else:
                r = m
        intervals.insert(l,newInterval)
        ans = []
        for i,j in intervals:
            if not ans or i > ans[-1][-1]:
                ans.append([i,j])
            else:
                ans[-1][-1] = max(ans[-1][-1],j)
        return ans