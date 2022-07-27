class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.pre_sum[i+1] = self.pre_sum[i]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right+1]-self.pre_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)