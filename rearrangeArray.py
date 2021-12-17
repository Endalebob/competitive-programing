Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def rearrangeArray(self, nums):
        nums.sort()
        for i in range(1,len(nums)-1,2):  
                nums[i+1], nums[i] = nums[i],nums[i+1] 
        return nums