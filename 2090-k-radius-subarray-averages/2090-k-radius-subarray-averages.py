class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<2*k+1:
            return [-1]*len(nums)
        less = [-1]*k
        summ = 0
        ans = []
        for i in range(2*k+1):
            summ += nums[i]
        ans.append(summ//(2*k+1))
        for i in range(k,len(nums)-k-1):
            summ -= nums[i-k]
            summ += nums[i+k+1]
            ans.append(summ//(2*k+1))
        return less + ans + less