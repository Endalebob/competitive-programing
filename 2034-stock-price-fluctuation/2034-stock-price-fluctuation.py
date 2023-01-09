class StockPrice:

    def __init__(self):
        self.dic = {}
        self.curr = 0
        self.counter = defaultdict(int)
        self.max_heap,self.min_heap = [],[]
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.dic:
            self.counter[self.dic[timestamp]] -= 1
        self.curr = max(self.curr,timestamp)
            
        self.dic[timestamp] = price
        self.counter[price] += 1
        heapq.heappush(self.max_heap,-price)
        heapq.heappush(self.min_heap,price)

    def current(self) -> int:
        return self.dic[self.curr]

    def maximum(self) -> int:
        while self.max_heap and self.counter[-1*self.max_heap[0]] <= 0:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0]

    def minimum(self) -> int:
        while self.min_heap and self.counter[self.min_heap[0]] <= 0:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()