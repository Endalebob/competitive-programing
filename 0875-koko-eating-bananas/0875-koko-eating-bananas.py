class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l,r = 1,piles[-1]
        while l<r:
            m = l + (r-l)//2
            cnt = 0
            i = 0
            while i < len(piles) and cnt <= h:
                cnt += ceil(piles[i]/m)
                i += 1
            if cnt <= h:
                r = m
            else:
                l = m + 1
        return l