class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        left = time[0]
        right = left*totalTrips
        mid = (left+right)//2
        def check(mid):
            total = 0
            for i in time:
                total += (mid//i)
                if total>=totalTrips:
                    return True
            return False
        while left<right:
            if check(mid):
                right = mid
            else:
                left = mid+1
            mid = (left+right)//2
        return mid