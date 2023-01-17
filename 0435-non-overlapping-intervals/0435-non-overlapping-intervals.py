class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''approach
        1: sort the entervals
        2: iterate to all elements starting from the second elements
        3: check if the end of the previous element is greater than the 
            start of the current element
                if it is increament counter by one
        4: return the number of count
        '''
        
        intervals.sort()
        prev = 0
        ans = 0
        for i in range(1,len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                if intervals[i][1]<intervals[prev][1]:
                    prev = i
                ans += 1
            else:
                prev = i
        return ans
        