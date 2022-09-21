class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)):
                l = j+1
                r = len(nums)-1
                while l<r:
                    tot = nums[i]+nums[j]+nums[l]+nums[r]
                    if tot == target:
                        ans.add((nums[i],nums[j],nums[l],nums[r]))
                    if tot > target:
                        r -= 1
                    else:
                        l += 1
        return ans