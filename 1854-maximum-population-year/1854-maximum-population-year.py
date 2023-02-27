class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pref = [0]*101
        ans = 1950
        for i,j in logs:
            pref[i-ans] += 1
            pref[j-ans] -= 1
        ans,val = 0,0
        for i in range(101):
            val += pref[i]
            if val > pref[ans]:
                ans = i
                pref[ans] = val
                
        return ans + 1950