Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sortColors(self, nums):
        
        for j in range(len(nums)-1):
            for i in range(j+1,len(nums)):
                if nums[j] > nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
        return nums