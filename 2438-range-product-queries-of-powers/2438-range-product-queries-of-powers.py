class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = []
        while n != 0:
            u = pow(2,int(log2(n)))
            arr.append(u)
            n -= u
        arr = arr[::-1]
        print(arr)
        nn = pow(2, int(ceil(log2(len(arr)))))
        n = 4*nn-1
        mm = n+1
        
        seg_tree = [1]*((n+1)//2)
        for i in range((n+1)//4,((n+1)//4)+len(arr)):
            seg_tree[i] = arr[i-((n+1)//4)]
        n = (n+1)//4
        while n != 0:
            for i in range(1,n):
                seg_tree[i] = seg_tree[2*i]*seg_tree[2*i+1]
            n //= 2
        def query(node, l_query, r_query, l_node, r_node):
            if l_node > r_query or r_node < l_query:
                return 1
            if l_query <= l_node <= r_node <= r_query:
                return seg_tree[node]
            lowest = (r_node + l_node) // 2
            return query(node * 2, l_query, r_query, l_node, lowest)*query(node * 2 + 1, l_query, r_query, lowest + 1, r_node)
        ans = []
        for l,r in queries:
            ans.append(query(1,l,r,0,len(seg_tree)//2-1)%(10**9+7))
        return ans