class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                tot = nums[i] + nums[l] + nums[r]
                if tot == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    while r>0 and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif tot<0:
                    l += 1
                else:
                    r -= 1
        return ans