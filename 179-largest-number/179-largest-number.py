class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        dic = {}
        so = []
        ans = ''
        for i,v in enumerate(nums):
            value = ''+str(v)
            m = value
            while len(value)<10:
                for j in m:
                    if len(value)==10:
                        break
                    value = value + j
            if value not in dic:
                dic[value] = [i]
            else:
                dic[value].append(i)
            so.append(value)
        so.sort()
        for i in so[::-1]:
            while dic[i]:
                ans += str(nums[dic[i].pop()])
        while len(ans)>1 and ans[0] == '0':
            ans = ans[1:]
        return ans