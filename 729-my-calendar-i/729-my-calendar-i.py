class MyCalendar:

    def __init__(self):
        self.seg = defaultdict(int)
        self.lazy = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        def find(node,lower,upper,start,end):
            if start > upper or end < lower:
                return 0
            if start <= lower and end >= upper:
                return self.seg[node]
            mid = (lower+upper)//2
            return self.lazy[node] + max(find(node*2,lower,mid,start,end), find(node*2+1,mid+1,upper,start,end))
        def update(node,lower,upper,start,end):
            if start > upper or end < lower:
                return 0
            if start <= lower and end >= upper:
                self.seg[node] += 1
                self.lazy[node] += 1
                return self.seg[node]
            else:
                mid = (lower+upper)//2
                self.seg[node] = self.lazy[node] + max(update(node*2,lower,mid,start,end),             update(node*2+1,mid+1,upper,start,end))
            return self.seg[node]
        if find(1,0,10**9+1,start,end-1) >= 1:
            return False
        update(1,0,10**9+1,start,end-1)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)