class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def perm(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            temp = []
            for i in range(len(nums)):
                current = nums[i]
                new = nums[:i] + nums[i+1:]
                pem = perm(new)
                for i in pem:
                    i.append(current)
                    temp.append(i)
            return temp
        new = perm(nums)
        ret = []
        vstd = set()
        for i in new:
            tup = tuple(i)
            if tup not in vstd:
                vstd.add(tup)
                ret.append(i)
        return ret
    