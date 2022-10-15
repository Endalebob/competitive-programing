class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        cnt = 0
        for i in nums:
            if i > 0:
                s.add(i)
        m = max(nums)+1
        for i in range(1,m+1):
            if i not in s:
                return i
        return 1