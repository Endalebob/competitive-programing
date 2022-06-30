import bisect
class MedianFinder:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        bisect.insort(self.nums,num)

    def findMedian(self) -> float:
        temp = len(self.nums) // 2
        if len(self.nums) % 2 == 0:
            return (self.nums[temp-1]+self.nums[temp])/2
        return self.nums[temp]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()