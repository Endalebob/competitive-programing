class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        right = values[-1] - len(values)+1
        ans = 0
        for i in range(len(values)-2,-1,-1):
            ans = max(ans,right+values[i]+i)
            right = max(right,values[i]-i)
        return ans