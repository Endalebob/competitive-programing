class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def perm(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            temp = []
            vstd = set()
            for i in range(len(nums)):
                if nums[i] not in vstd:
                    vstd.add(nums[i])
                    current = nums[i]
                    new = nums[:i] + nums[i+1:]
                    pem = perm(new)
                    for i in pem:
                        i.append(current)
                        temp.append(i)
            return temp
        return perm(nums)