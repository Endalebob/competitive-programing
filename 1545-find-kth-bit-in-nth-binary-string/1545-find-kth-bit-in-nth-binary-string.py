class Solution:
    def invert(self, l):
        return l + '1' + l[:len(l)//2] + "0" + l[len(l)//2+1:]
    def findKth(self,n):
        if n == 1:
            return '0'
        if n == 2:
            return '011'
        return self.invert(self.findKth(n-1))
    def findKthBit(self, n: int, k: int) -> str:
        return (self.findKth(n))[k-1]