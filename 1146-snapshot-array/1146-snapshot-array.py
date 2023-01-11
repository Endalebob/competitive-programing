class SnapshotArray:

    def __init__(self, length: int):
        self.sna = {}
        self.snaps = []
        

    def set(self, index: int, val: int) -> None:
        self.sna[index] = val

    def snap(self) -> int:
        self.snaps.append(deepcopy(self.sna))
        return len(self.snaps)-1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)