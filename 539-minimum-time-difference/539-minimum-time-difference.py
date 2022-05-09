class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minimum = [int(s[:2])*60+int(s[-2]+s[-1]) for s in timePoints]
        minimum.sort()
        ans = minimum[-1]-minimum[0]
        ans = min(ans,24*60-ans)
        print(minimum)
        for i in range(len(minimum)-1):
            ans = min(ans,minimum[i+1] - minimum[i])
        return ans