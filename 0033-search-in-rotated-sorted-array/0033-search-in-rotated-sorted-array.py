class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<r:
            m = (r+l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        def bs(l,r):
            while l<=r:
                m = (r+l)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return -1
        ans = bs(0,l)
        if ans != -1:
            return ans
        return bs(l,len(nums)-1)