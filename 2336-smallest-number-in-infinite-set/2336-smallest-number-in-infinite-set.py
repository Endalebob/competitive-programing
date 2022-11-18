class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [i for i in range(1,1001)]
        self.removed = set()
        heapq.heapify(self.nums)

    def popSmallest(self) -> int:
        curr = heapq.heappop(self.nums)
        self.removed.add(curr)
        return curr

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
            heapq.heappush(self.nums,num)
