class RandomizedCollection:

    def __init__(self):
        self.storeVal = defaultdict(list)
        self.storeIndex = {}
        self.count = 0

    def insert(self, val: int) -> bool:
        if len(self.storeVal[val]) > 0:
            self.storeVal[val].append(self.count)
            self.storeIndex[self.count] = val
            self.count += 1
            return False
        self.storeVal[val].append(self.count)
        self.storeIndex[self.count] = val
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        if self.storeVal[val]:
            temp = self.storeVal[val].pop()
            self.storeIndex[temp],self.storeIndex[self.count-1] = self.storeIndex[self.count-1],self.storeIndex[temp]
            self.storeIndex.pop(self.count-1)
            if temp in self.storeIndex:
                self.storeVal[self.storeIndex[temp]].pop()
                bisect.insort(self.storeVal[self.storeIndex[temp]], temp)
            self.count -= 1
            return True
        return False

    def getRandom(self) -> int:
        return self.storeIndex[randint(0,len(self.storeIndex)-1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()