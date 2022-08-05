class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def rec(s,g):
            if s > target:
                return 0
            if s == target:
                return 1
            temp = 0
            for i in nums:
                temp += rec(s+i,i)
            return temp
        return rec(0,0)