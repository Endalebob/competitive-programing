class MyCircularQueue:

    def __init__(self, k: int):
        self.deq = deque()
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.k<=len(self.deq):
            return False
        self.deq.append(value)
        return True

    def deQueue(self) -> bool:
        if self.deq:
            self.deq.popleft()
            return True
        return False

    def Front(self) -> int:
        if self.deq:
            return self.deq[0]
        return -1

    def Rear(self) -> int:
        if self.deq:
            return self.deq[-1]
        return -1

    def isEmpty(self) -> bool:
        return not self.deq

    def isFull(self) -> bool:
        return len(self.deq) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()