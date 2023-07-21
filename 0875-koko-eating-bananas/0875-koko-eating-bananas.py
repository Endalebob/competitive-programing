class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_possible(m):
            curr = 0
            for i in piles:
                curr += ceil(i/m)
            return curr<=h
        l,r = 1,max(piles)
        while l<r:
            m = l+(r-l)//2
            if is_possible(m):
                r = m
            else:
                l = m+1
        return l
        