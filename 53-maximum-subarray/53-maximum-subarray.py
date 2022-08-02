class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = [nums[0]]
        def rec(idx):
            if idx == len(nums)-1:
                ans[0] = max(ans[0],nums[idx])
                return nums[idx]
            a = nums[idx]+max(rec(idx+1),0)
            ans[0] = max(ans[0],a)
            return a
        rec(0)
        return ans[0]