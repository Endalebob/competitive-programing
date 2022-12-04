class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pref_sum,suf_sum = [nums[0]],[nums[-1]]
        for i in range(1,len(nums)):
            pref_sum.append(pref_sum[-1]+nums[i])
            suf_sum.append(suf_sum[-1]+nums[-1-i])
        ans = float('inf')
        ret = 0
        for i in range(len(nums)):
            n = len(nums)-i-1
            if n == 0:
                a = 0
            else:
                a = (suf_sum[n-1])//n 
            if abs((pref_sum[i])//(i+1) - a) < ans:
                ans = abs((pref_sum[i])//(i+1) - a)
                ret = i
        return ret