class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l,r = 0,len(nums)-1
        mid = (l+r)//2
        while l<r:
            if nums[mid]>t:
                if nums[r]<t or nums[r]>nums[mid]:
                    r = mid
                else:
                    l = mid+1
            elif nums[mid]<t:
                if nums[r]>=t or nums[l]<nums[mid]:
                    l = mid+1
                else:
                    r = mid
            else:
                return mid
            mid = (l+r)//2
            
        if nums[mid] == t:
            return mid
        return -1