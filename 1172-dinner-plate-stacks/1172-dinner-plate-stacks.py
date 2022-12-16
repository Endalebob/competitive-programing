class DinnerPlates:

    def __init__(self, capacity: int):
        self.capa = capacity
        self.heap = [i for i in range(3*10**5)]
        heapq.heapify(self.heap)
        self.nums = []
        self.last = -1

    def push(self, val: int) -> None:
        if len(self.nums) <= self.heap[0]:
            self.nums.append([])
            self.last += 1
        self.nums[self.heap[0]].append(val)
        if len(self.nums[self.heap[0]]) == self.capa:
            heapq.heappop(self.heap)
            

    def pop(self) -> int:
        index = self.last
        if index>=0 and self.nums[index]:
            if len(self.nums[index]) == self.capa:
                heapq.heappush(self.heap,index)
            m = self.nums[index].pop()
            if not self.nums[index]:
                self.last -= 1
                self.nums.pop()
            return m
        if index>0 and self.nums[index-1]:
            if len(self.nums[self.heap[index-1]]) == self.capa:
                heapq.heappush(self.heap,index-1)
            m = self.nums[index-1].pop()
            return m
        return -1

    def popAtStack(self, index: int) -> int:
        if index < len(self.nums):
            if self.nums[index]:
                if len(self.nums[index]) == self.capa:
                    heapq.heappush(self.heap,index)
                m = self.nums[index].pop()
                if index == self.last:
                    if not self.nums[index]:
                        self.last -= 1
                        self.nums.pop()
                return m
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)