Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def minSetSize(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1 
        nwv = list(dic.values())
        nwv.sort()
        m = 0
        i = 0
        while m < len(nums)//2:
            m += nwv[-1-i]
            i += 1
        return i