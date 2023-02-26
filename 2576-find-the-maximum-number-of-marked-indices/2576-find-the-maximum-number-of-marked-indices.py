class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        hi = (len(nums)-1)//2 + 1
        r = len(nums)-1
        ans = 0
        while hi > 0 and r >= (len(nums)-1)//2+1:
            num = nums[r]//2
            idx = bisect_right(nums,num,lo=0,hi=hi)
            if idx > 0:
                ans += 2
                hi = idx-1
            else:
                break
            r -= 1
        return ans