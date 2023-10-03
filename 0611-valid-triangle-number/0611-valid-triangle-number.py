class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)-1,1,-1):
            l,r = 0,i-1
            while l < r:
                if nums[i] >= nums[l]+nums[r]:
                    l += 1
                else:
                    ans += (r-l)
                    r -= 1
        return ans
            