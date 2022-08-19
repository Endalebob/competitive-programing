class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = max(piles)
        mid = (left+right)//2
        ans = right
        while left<right:
            temp = 0
            for i in range(len(piles)):
                if piles[i]<=mid:
                    temp += 1
                else:
                    temp += (piles[i]//mid)
                    if piles[i]%mid != 0:
                        temp += 1
            if temp <= h:
                ans = min(ans,mid)
                right = mid
            else:
                left = mid+1
            mid = (left+right)//2
        return ans
                