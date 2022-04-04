class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int: 
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                mx = max(nums[-1] - k, nums[i]   + k)
                mn = min(nums[0]  + k, nums[i+1] - k)
                ans = min(ans, mx - mn)
        return ans