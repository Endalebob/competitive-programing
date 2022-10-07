class MyCalendarTwo:

    def __init__(self):
        self.seg = defaultdict(int)
        self.lazy = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        def update(node,lower,upper,start,end):
            if start>upper or end<lower:
                return
            if start<=lower and end>=upper:
                self.seg[node] += 1
                self.lazy[node] += 1
            else:
                mid = (lower+upper)//2
                update(node*2,lower,mid,start,end)
                update(node*2+1,mid+1,upper,start,end)
                self.seg[node] = self.lazy[node]+max(self.seg[node*2],self.seg[node*2+1])
        def find(node,lower,upper,start,end):
            if start>upper or end<lower:
                return 0
            if start<=lower and end>=upper:
                return self.seg[node]
            else:
                mid = (lower+upper)//2
                return self.lazy[node]+ max(find(node*2,lower,mid,start,end), find(node*2+1,mid+1,upper,start,end))
        if find(1,0,10**9+1,start,end-1) == 2:
            return False
        update(1,0,10**9+1,start,end-1)
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)