class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l,r = 0,len(nums)-1
        ans = [-1,-1]
        while l<r:
            m = l+(r-l)//2
            if nums[m] < target:
                l = m+1
            else:
                r = m
        if nums[l] == target:
            ans[0] = l
        
        l,r = 0,len(nums)-1
        while l<r:
            m = l+(r-l)//2
            if nums[m] <= target:
                l = m+1
            else:
                r = m
        
        if nums[l] == target:
            ans[1] = l
        elif nums[l-1] == target:
                ans[1] = l-1
            
        return ans