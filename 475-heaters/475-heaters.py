class Solution:
    def findRadius(self, houses: List[int], heater: List[int]) -> int:
        houses.sort()
        heater.sort()
        ret = 0
        curr = 0
        for i in houses:
            val = float('inf')
            for j in range(curr, len(heater)):
                if val < abs(i - heater[j]):
                    break
                else:
                    curr = j
                    val = abs(i - heater[j])
            ret = max(ret, val)
        return ret