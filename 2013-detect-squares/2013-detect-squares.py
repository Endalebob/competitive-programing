class DetectSquares:

    def __init__(self):
        self.dic = {}
        
        
        

    def add(self, point: List[int]) -> None:
        if tuple(point) in self.dic:
            self.dic[tuple(point)] += 1
        else:
            self.dic[tuple(point)] = 1

    def count(self, point: List[int]) -> int:
        ans = 0
        for i in self.dic:
            x,y = i
            if x != point[0] and y != point[1] and abs(x -point[0]) == abs(y - point[1]):
                if (x,y) in self.dic and (x,point[1]) in self.dic and (point[0],y) in self.dic:
                    ans += self.dic[(x,y)] * self.dic[(x,point[1])] * self.dic[(point[0],y)]
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)