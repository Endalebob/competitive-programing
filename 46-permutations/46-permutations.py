class Solution:
    def perms(self,nums,ans):
        if len(nums) == 1:
            return [[nums[0]]]
        for i in range(len(nums)):
            n = nums.popleft()
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            ans.extend(perms)
            nums.append(n)
        return ans
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = deque(nums)
        return self.perms(nums,[])
            