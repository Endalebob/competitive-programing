class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum = [0] * (len(nums)+1)
        pre_sum2 = [0] * (len(nums)+1)
        for i in range(len(nums)):
            pre_sum[i+1] = nums[i]+pre_sum[i]
        for i in range(len(nums),0,-1):
            pre_sum2[i-1] = nums[i-1]+pre_sum2[i]
        for i in range(len(nums)):
            if pre_sum[i] == pre_sum2[i+1]:
                return i
        return -1
        