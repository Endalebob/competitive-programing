class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while r>l and nums[r] == nums[r+1]:
                        r -= 1
        return ans