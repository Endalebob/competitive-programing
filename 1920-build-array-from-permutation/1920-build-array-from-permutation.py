class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # a = a+n*b
        n = len(nums)
        for i in range(n):
            nums[i] += n*(nums[nums[i]]%n)
        for i in range(n):
            nums[i] //= n
        return nums
        