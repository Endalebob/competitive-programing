class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ans = [0]
        memo = {}
        def rec(s,g):
            if (s,g) in memo:
                return memo[(s,g)]
            if s > target:
                return 0
            if s == target:
                return 1
            temp = 0
            for i in nums:
                temp += rec(s+i,i)
            memo[(s,g)] = temp
            return temp
        # rec(0,0)
        return rec(0,0)