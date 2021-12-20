Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        while len(nums)>1:
            if nums[0]+nums[-1]>k:
                nums.pop(len(nums)-1)
            elif nums[0]+nums[-1]<k:
                nums.pop(0)
            else:
                nums.pop(len(nums)-1)
                nums.pop(0)
                count += 1
        return count