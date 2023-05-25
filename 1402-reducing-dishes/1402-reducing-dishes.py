class Solution:
    def maxSatisfaction(self, arr: List[int]) -> int:
        arr.sort(reverse = True)
        curr = 0
        ans = 0
        for i in arr:
            curr += i
            if curr > 0:
                ans += curr
            else:
                return ans
        return ans