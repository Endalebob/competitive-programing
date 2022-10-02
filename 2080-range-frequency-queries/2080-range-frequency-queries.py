class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.len = len(arr)-1
        n = len(arr)
        n = pow(2,int(ceil(log2(len(arr)))))
        self.seg_tree = [{} for i in range(2*n)]
        for i in range(n,n+len(arr)):
            self.seg_tree[i][arr[i-n]] = 1
        def update(a, b):
            ret = {}
            for i in a:
                ret[i] = a[i]
            for j in b:
                if j in ret:
                    ret[j] += b[j]
                else:
                    ret[j] = b[j]
            return ret

        while n != 0:
            for i in range(1,n):
                self.seg_tree[i] = update(self.seg_tree[i*2],self.seg_tree[i*2+1])
            n //= 2
    def query(self, left: int, right: int, val: int) -> int:
        def find(node,lower,upper,l_query,r_query):
            if l_query > upper or r_query < lower or val not in self.seg_tree[node]:
                return 0
            if l_query <= lower and r_query >= upper:
                if val in self.seg_tree[node]:
                    return self.seg_tree[node][val]
                return 0
            mid = (lower + upper)//2
            return find(node*2,lower,mid,l_query,r_query) + find(node*2+1,mid+1,upper,l_query,r_query)
        return find(1,0,len(self.seg_tree)//2-1,left,right)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)