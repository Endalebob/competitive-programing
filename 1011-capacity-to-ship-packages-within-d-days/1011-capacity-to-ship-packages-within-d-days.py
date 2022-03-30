class Solution:
    def isPossible(self,weight,day,mid):
        count = 0
        i = 0
        while i<len(weight):
            sums = 0
            while i<len(weight) and mid>=sums:
                sums += weight[i]
                if mid>=sums:
                    i += 1
            count += 1
        return count <= day
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        mid = (left + right)//2
        ans = right
        while left<right:
            if self.isPossible(weights,days,mid):
                right = mid
                ans = min(ans,mid)
            else:
                left = mid+1
            mid = (left + right)//2
        if self.isPossible(weights,days,mid):
                ans = min(ans,mid)
        return ans