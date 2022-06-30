class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # nums = set(nums)
        # ma = max(nums)+1
        # mi = min(nums)
        # sub = mi
        # ret = 0
        # for i in range(mi,ma):
        #     if i in nums:
        #         ret = max(ret,i-sub)
        #         sub = i
        # return ret
        nums.sort()
        ans = 0
        for i in range(len(nums)-1):
            ans = max(ans,nums[i+1]-nums[i])
        return ans