class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        for i in range(k):
            summ += nums[i]
        ans = summ/k
        for i in range(k,len(nums)):
            temp = nums[i] - nums[i-k]
            summ += temp
            ans = max(ans,summ/k)
        return ans
        