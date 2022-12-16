class MyQueue:

    def __init__(self):
        self.nums = []
        self.idx = 0

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> int:
        self.idx += 1
        return self.nums[self.idx-1]

    def peek(self) -> int:
        return self.nums[self.idx]

    def empty(self) -> bool:
        return len(self.nums) - self.idx == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()