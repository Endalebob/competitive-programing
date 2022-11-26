class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def find(idx):
            ans = 1000
            ret = idx+1
            for i in range(idx+1,len(nums)):
                if  nums[i] > nums[idx] and nums[i] < ans:
                    ans = nums[i]
                    ret = i
            return ret
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i-1]:
                idx = find(i-1)
                nums[idx],nums[i-1] = nums[i-1],nums[idx]
                nums[i:] = sorted(nums[i:])
                return
            i -= 1
        for i in range(len(nums)//2):
            nums[i],nums[-1-i] = nums[-1-i], nums[i]
        