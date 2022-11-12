import bisect
class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums,num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2:
            return self.nums[n//2]
        return (self.nums[n//2] + self.nums[n//2 - 1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()