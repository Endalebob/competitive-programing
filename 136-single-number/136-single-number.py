class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = set()
        for i in nums:
            if i in check:
                check.remove(i)
            else:
                check.add(i)
        for i in check:
            return i