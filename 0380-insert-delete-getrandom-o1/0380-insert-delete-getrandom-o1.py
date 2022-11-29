class RandomizedSet:

    def __init__(self):
        self.idx = {}
        self.val = []

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.val)
        self.val.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        self.val[self.idx[val]],self.val[-1] = self.val[-1],self.val[self.idx[val]]
        self.idx[self.val[self.idx[val]]] = self.idx[self.val[-1]] 
        self.idx.pop(val)
        self.val.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.val)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()