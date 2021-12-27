Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        dic = {}
        com = len(nums)/3
        for i, v in enumerate(nums):
            if v not in dic:
                dic[v] = 1
            else:
                dic[v] += 1
        for i in dic:
            if dic[i]>com:
                ans.append(i)
        return ans