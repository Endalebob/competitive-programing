Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class MinStack:

    def __init__(self):
        self.node = []

    def push(self, val: int) -> None:
        return self.node.append(val)

    def pop(self) -> None:
        return self.node.pop()

    def top(self) -> int:
        return self.node[-1]

    def getMin(self) -> int:
        return min(self.node)