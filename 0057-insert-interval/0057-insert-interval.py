class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:
        n = len(intervals)
        for i in range(len(intervals)):
            start,end = intervals[i]
            if ni[0] < start:
                intervals.insert(i,ni)
                break
        if n == len(intervals):
            intervals.append(ni)
        delete = []
        for i in range(n):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = intervals[i][0]
                intervals[i][1] = max(intervals[i][1],intervals[i+1][1])
                intervals[i+1][1] = max(intervals[i][1],intervals[i+1][1])
                delete.append(i)
                
        for i in delete[::-1]:
            intervals.pop(i)
        return intervals