class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        if not nums:
            return ans
        def first():
            l,r = 0,len(nums)-1
            while r>l:
                m = l+(r-l)//2
                if nums[m]<target:
                    l = m+1
                else:
                    r = m
            if nums[l] == target:
                ans[0] = l
        def last():
            l,r = 0,len(nums)
            while r>l:
                m = l+(r-l)//2
                if nums[m]<=target:
                    l = m+1
                else:
                    r = m
            if nums[l-1] == target:
                ans[1] = l-1
        first()
        last()
        return ans
        