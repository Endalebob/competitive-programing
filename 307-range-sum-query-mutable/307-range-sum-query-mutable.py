class SegmentTree:
    def __init__(self, arr, append):
        self.seg_tree = defaultdict(int)

    def build(self):
        n = len(self.arr)
        for i in range(len(self.arr), len(self.arr)*2):
            self.seg_tree[i] = self.arr[i - n]
        while n != 0:
            for i in range(1, n):
                self.seg_tree[i] = min(self.seg_tree[2 * i] , self.seg_tree[2 * i + 1])
            n //= 2

    def query(self, lq, rq):
        a, b = 0, len(self.arr) - 1

        def find(node, lq, rq, ls, rs):
            if rs < lq or ls > rq:
                return self.append
            if lq >= ls and rs >= rq:
                return self.seg_tree[node]
            v = (lq + rq) // 2
            return min(find(node * 2, lq, v, ls, rs) , find(node * 2 + 1, v + 1, rq, ls, rs))

        return find(1, a, b, lq, rq)

class NumArray:

    def __init__(self, nums: List[int]):
        while len(nums) & (len(nums)-1) != 0:
            nums.append(0)
        self.tree = [0]*(2*len(nums))
        for i in range(len(nums)):
            self.tree[len(nums)+i] = nums[i]
        for i in range(len(nums)-1,0,-1):
            self.tree[i] = self.tree[2*i]+self.tree[2*i+1]
    def update(self, index: int, val: int) -> None:
        n = len(self.tree)//2+index
        self.tree[n] = val
        while n != 0:
            h = n//2
            self.tree[h] = self.tree[h*2]+self.tree[h*2+1]
            n //= 2

    def sumRange(self, left: int, right: int) -> int:
        return self.segmentTree(1,len(self.tree)//2-1,0,right,left)
    def segmentTree(self,node,n_high,n_low,q_high,q_low):
        if n_high<=q_high and n_low>=q_low:
            return self.tree[node]
        elif n_high<q_low or n_low>q_high:
            return 0
        h = (n_high+n_low)//2
        return self.segmentTree(node*2,h,n_low,q_high,q_low) + self.segmentTree(node*2+1,n_high,h+1,q_high,q_low)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)