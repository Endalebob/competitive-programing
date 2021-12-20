Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]+nums[-1]
        for i in range(len(nums)//2):
            if nums[i]+nums[len(nums)-(i+1)]>a:
                a = nums[i]+nums[len(nums)-(i+1)]
        return a