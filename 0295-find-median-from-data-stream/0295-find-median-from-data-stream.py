from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.nums = SortedList([])

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2:
            return self.nums[n//2]
        return (self.nums[n//2] + self.nums[n//2 - 1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()