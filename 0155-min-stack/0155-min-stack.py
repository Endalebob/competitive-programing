class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class MinStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.mono_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mono_stack or self.mono_stack[-1] > val:
            self.mono_stack.append(val)
        self.count[val] += 1
        

    def pop(self) -> None:
        popped = self.stack.pop()
        self.count[popped] -= 1
        while self.mono_stack and self.count[self.mono_stack[-1]] == 0:
            self.mono_stack.pop()
        return popped
        
            
            
            
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mono_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()