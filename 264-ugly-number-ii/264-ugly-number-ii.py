class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nthugly = 1
        uglyMake = [2,3,5] #We make uglyNumber by using these number.
        hold = [2,3,5]
        heapq.heapify(hold)
        i = 1
        while i<n:
            check = heapq.heappop(hold)
            while nthugly == check:
                check = heapq.heappop(hold)
            nthugly = check
            temp = [i*nthugly for i in uglyMake]
            while temp:
                heapq.heappush(hold,temp.pop())
            i += 1
        return nthugly
        
        
        