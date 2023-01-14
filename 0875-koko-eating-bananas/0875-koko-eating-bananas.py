class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        def is_possible(speed):
            curr = 0
            i = 0
            while curr <= h and i<len(piles):
                curr += math.ceil(piles[i]/speed)
                i += 1
            if curr <= h and i == len(piles):
                return True
            return False
                
        while l < r:
            m = l + (r-l)//2
            if is_possible(m):
                r = m
            else:
                l = m + 1
        return l
            
            