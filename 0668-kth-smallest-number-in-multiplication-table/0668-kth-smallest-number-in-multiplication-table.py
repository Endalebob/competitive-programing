class Solution:
    def findKthNumber(self, mm: int, n: int, k: int) -> int:
        def is_possible(m):
            curr = 0
            i = 1
            while curr < k and m//i and i<=mm:
                curr += min(m//i,n)
                i += 1
            if curr < k:
                return False
            return True
        l,r = 1,mm*n
        while l < r:
            m = l + (r-l)//2
            if is_possible(m):
                r = m
            else:
                l = m+1
        return l
                