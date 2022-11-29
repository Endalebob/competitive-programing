class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(k,i):
            if i == -1:
                return startFuel
            if k == 0:
                return startFuel
            return max(dp(k-1,i-1)+stations[i][1] if dp(k-1,i-1)>=stations[i][0] else 0,dp(k,i-1))
        for i in range(len(stations)+1):
            if dp(i,len(stations)-1) >= target:
                return i
        return -1