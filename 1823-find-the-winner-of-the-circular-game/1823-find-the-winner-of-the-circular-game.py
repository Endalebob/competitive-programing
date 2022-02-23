class Solution:
    def helper(self,nums,k,pointer):
        if len(nums) == 1:
            return nums[0]
        m = 0
        for i in range(len(nums)):
            pointer += 1
            m += 1
            if pointer == k:
                m -= 1
                pointer = 0
                nums.pop(m)
        return self.helper(nums,k,pointer)
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [m for m in range(1,n+1)]
        if k==1:
            return n
        return self.helper(nums,k,0)