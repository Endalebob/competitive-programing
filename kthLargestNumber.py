Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort()
        nums.reverse()
        return str(nums[k-1])