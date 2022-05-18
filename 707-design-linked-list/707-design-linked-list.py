class MyLinkedList:

    def __init__(self):
        self.stack = []

    def get(self, index: int) -> int:
        if len(self.stack)>index:
            return self.stack[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.stack = [val] + self.stack

    def addAtTail(self, val: int) -> None:
        self.stack.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if len(self.stack)>=index:
            self.stack.insert(index,val)
        else: return
            

    def deleteAtIndex(self, index: int) -> None:
        if len(self.stack)>index:
            self.stack.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)