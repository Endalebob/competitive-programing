class MyCalendarThree:

    def __init__(self):
        self.seg = defaultdict(int)
        self.lazy = defaultdict(int)
    

    def book(self, start: int, end: int) -> int:
        def update(node,lower, upper,start,end):
            if start > upper or end < lower:
                return
            if start <= lower and end>=upper:
                self.seg[node] += 1
                self.lazy[node] += 1
            else:
                mid = (lower+upper)//2
                update(node*2,lower,mid,start,end)
                update(node*2+1,mid+1,upper,start,end)
                self.seg[node] = self.lazy[node ] + max(self.seg[node*2],self.seg[node*2+1])
        update(1,0,10**9,start,end-1)
        return self.seg[1]


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)