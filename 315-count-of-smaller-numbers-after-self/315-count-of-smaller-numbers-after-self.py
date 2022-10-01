class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        mi = min(nums)
        for i in range(len(nums)):
            nums[i] -= mi
        mi = 0
        ma = max(nums)
        self.n = ma+1
        def build():
            self.n = pow(2,int(ceil(log2(self.n))))
            seg_tree = [0]*2*self.n
            return seg_tree
        def find(node,lower,upper,l_query,r_query):
            if l_query>upper or r_query<lower:
                return 0
            if l_query<=lower and r_query>=upper:
                return seg_tree[node]
            mid = (lower+upper)//2
            return find(node*2,lower,mid,l_query,r_query) + find(node*2+1,mid+1,upper,l_query,r_query)
        
        
        def update(node,lower,upper,l_query,r_query):
            if l_query>upper or r_query<lower:
                return seg_tree[node]
            if l_query<=lower and r_query>=upper:
                seg_tree[node]+=1
                return seg_tree[node]
            mid = (lower+upper)//2
            seg_tree[node] = update(node*2,lower,mid,l_query,r_query) +update(node*2+1,mid+1,upper,l_query,r_query) 
            return seg_tree[node]
        seg_tree = build()
        ans = []
        for i in nums[::-1]:
            val = len(seg_tree)//2-1
            ans.append(find(1,mi,val,mi,i-1))
            update(1,mi,val,i,i)
        return ans[::-1]
    