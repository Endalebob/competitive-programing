class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        add=0
        for i in w:
            add += i
            self.w.append(add)

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.w,random.randint(1,self.w[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()