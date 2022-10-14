class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        l,r = 0,len(nums)-1
        mid = len(nums)
        while l<=r:
            mid = l +(r-l)//2
            if nums[mid] >= target:
                r = mid-1
            else:
                l = mid+1
        if mid<len(nums) and nums[mid] == target:
            ans[0] = mid
        elif mid+1<len(nums) and nums[mid+1] == target:
            ans[0] = mid+1
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l +(r-l)//2
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        if mid<len(nums) and nums[mid] == target:
            ans[1] = mid
        elif mid-1>=0 and nums[mid-1] == target:
            ans[1] = mid-1
        return ans
        
        