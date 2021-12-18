Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def checkArithmeticSubarrays(nums, l, r):
        li = []
        for i in range(len(l)):
            m=nums[l[i]:r[i]+1]
            m.sort()
            if len(m)==2:
                li.append(True)
            for j in range(len(m)-2):
                mm=(m[j]-m[j+1]==m[j+1]-m[j+2])
                if mm==False:
                    li.append(False)
                    break
                if j+3 == len(m) and mm:
                    li.append(True)
        return li