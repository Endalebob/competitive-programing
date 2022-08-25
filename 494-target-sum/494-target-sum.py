class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = {}
        def rec(idx,s):
            if idx == len(nums) and s == target:
                return 1
            if idx == len(nums):
                return 0
            if (idx,s) in dic:
                return dic[(idx,s)]
            dic[(idx,s)] = rec(idx+1,s-nums[idx]) + rec(idx+1,s+nums[idx])
            return dic[(idx,s)]
        return rec(0,0)