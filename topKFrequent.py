Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = set(nums)
        dic = {}
        for i in unique:
            dic[i] = nums.count(i)
        nwv = list(dic.values())
        nwk = list(dic.keys())
        check = nwv[:]
        check.sort()
        ld = []
        for i in range(k):
            m = nwv.index(check[-1-i])
            nwv[m] = 0
            ld.append(nwk[m])
        return ld 