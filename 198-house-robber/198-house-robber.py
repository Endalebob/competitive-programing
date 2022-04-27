class Solution:
    def gain(self,i,dic,nums):
        if i>=len(nums):
            return 0
        if i in dic:
            return dic[i]
        dic[i] = max(self.gain(i+2,dic,nums), self.gain(i+3,dic,nums)) +nums[i]
        return dic[i]
    def rob(self, nums: List[int]) -> int:
        dic = {}
        return max(self.gain(0,dic,nums),self.gain(1,dic,nums))
