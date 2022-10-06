from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.dic_key = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic_key:
            self.dic_key[key] = SortedDict()
        self.dic_key[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic_key:
            return ''
        idx = self.dic_key[key].bisect_right(timestamp)
        if idx == 0:
            return ''
        return self.dic_key[key].peekitem(idx-1)[1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)