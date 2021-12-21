Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        return self.stack1.append(x)

    def pop(self) -> int:
        self.stack2 = []
        if len(self.stack1)!= 0:
            while len(self.stack1)!= 0:
                self.stack2.append(self.stack1.pop())
            m = self.stack2.pop()
            while len(self.stack2)!= 0:
                self.stack1.append(self.stack2.pop())
            return m

    def peek(self) -> int:
        self.stack2 = []
        if len(self.stack1)!= 0:
            while len(self.stack1)!= 0:
                self.stack2.append(self.stack1.pop())
            m = self.stack2[-1]
            while len(self.stack2)!= 0:
                self.stack1.append(self.stack2.pop())
            return m
           
    def empty(self) -> bool:
        return (len(self.stack1) == 0)