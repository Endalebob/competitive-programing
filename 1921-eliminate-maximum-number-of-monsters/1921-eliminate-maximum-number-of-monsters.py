class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # speed = dist/time
        time = [d/s for d,s in zip(dist,speed)]
        time.sort()
        ans = 0
        curr = 0
        for i in time:
            if curr < i:
                ans += 1
            else:
                return ans
            curr += 1
        return ans