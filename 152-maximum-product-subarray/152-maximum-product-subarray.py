class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _min,_max,ans = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            curr = _min
            _min = min(nums[i],nums[i]*_min,nums[i]*_max)
            _max = max(nums[i],nums[i]*curr,nums[i]*_max)
            ans = max(ans,_max)
        return ans