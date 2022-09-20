class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        s = ''.join([chr(i) for i in nums1])
        ans = 0
        t = ''
        for i in nums2:
            t +=chr(i)
            if t in s:
                ans = max(ans,len(t))
            else:
                t = t[1:]
        return ans