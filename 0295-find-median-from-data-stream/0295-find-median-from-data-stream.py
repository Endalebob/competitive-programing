class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []
        self.k = 0

    def addNum(self, num: int) -> None:
        self.k = 1- self.k
        heapq.heappush(self.max,-num)
        curr = -heapq.heappop(self.max)
        heapq.heappush(self.min,curr)
        if self.k:
            curr = -heapq.heappop(self.min)
            heapq.heappush(self.max,curr)
        

    def findMedian(self) -> float:
        if self.k:
            return -self.max[0]
        else:
            return (self.min[0]-self.max[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()