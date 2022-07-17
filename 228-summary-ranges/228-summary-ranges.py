class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return
        rang = 1
        r,l = 0,0
        ans = []
        while r<len(nums)-1:
            if nums[r]+rang != nums[r+1]:
                if l!=r:
                    ans.append(str(nums[l])+'->'+str(nums[r]))
                else: ans.append(str(nums[l]))
                l = r+1
            r += 1
        if l!=r:
            ans.append(str(nums[l])+'->'+str(nums[r]))
        else: ans.append(str(nums[l]))
        return ans