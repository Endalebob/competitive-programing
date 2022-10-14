class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums,target+1)
        r = bisect_right(nums,target-1)
        ans = [-1,-1]
        if l-1>=0 and nums[l-1] == target:
            ans[1] = l-1
        if r<len(nums) and nums[r] == target:
            ans[0] = r
        return ans
        
        