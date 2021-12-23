Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        for i in nums1:
            ind = nums2.index(i)+1
            u = True
            for j in range(ind,len(nums2)):
                if nums2[j]>i:
                    ret.append(nums2[j])
                    u = False
                    break
            if u:
                ret.append(-1)
        return ret