class Solution:
    def maxx(self,nums,i,dic):
        if i>=len(nums):
            return 0
        if i in dic: return dic[i]
        dic[i] = nums[i] + max(self.maxx(nums,i+3,dic),self.maxx(nums,i+2,dic))
        return dic[i]
    def rob(self, nums: List[int]) -> int:
        dic = {}
        return max(self.maxx(nums,0,dic),self.maxx(nums,1,dic))