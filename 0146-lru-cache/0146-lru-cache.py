class LRUCache:
    
    def __init__(self, capacity: int):
        self.length = capacity
        self.dic = OrderedDict()
    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
                self.dic.move_to_end(key)
        elif len(self.dic)==self.length:
            self.dic.popitem(last=False)
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)