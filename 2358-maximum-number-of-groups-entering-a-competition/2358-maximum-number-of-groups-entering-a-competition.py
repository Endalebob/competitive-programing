class Solution:
    def maximumGroups(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        while n > k:
            k += 1
            n -= k
        return k
            