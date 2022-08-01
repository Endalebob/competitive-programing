class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo = {}
        def rec(idx,last):
            if idx>last:
                return 0
            if idx in memo:
                return memo[idx]
            memo[idx] = nums[idx]+max(rec(idx+2,last),rec(idx+3,last))
            return memo[idx]
        a = rec(0,len(nums)-2)
        memo = {}
        return max(a,rec(1,len(nums)-1),rec(2,len(nums)-1))