class MyCalendar:

    def __init__(self):
        self.calander = []

    def book(self, start: int, end: int) -> bool:
        a = bisect_right(self.calander,(start,end))
        if (a>0 and self.calander[a-1][1]>start) or (a<len(self.calander) and self.calander[a][0]<end):
            return False
        insort(self.calander,(start,end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)