Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MyCircularDeque:

    def __init__(self, k: int):
        self.node = []
        self.max = k
    def insertFront(self, value: int) -> bool:
        if len(self.node) < self.max:
            self.node.insert(0,value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.node) < self.max:
            self.node.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if len(self.node)>0:
            self.node.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.node)>0:
            self.node.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.node)>0:
            return self.node[0]
        return -1

    def getRear(self) -> int:
        if len(self.node)>0:
            return self.node[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.node)<=0

    def isFull(self) -> bool:
        return len(self.node) == self.max