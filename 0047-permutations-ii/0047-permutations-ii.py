class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def ans(num,temp,ret):
            if not num:
                ret.append(deepcopy(temp))
            vstd = set()
            for i in range(len(num)):
                new = num[:i]+num[i+1:]
                if num[i] in vstd:
                    continue
                vstd.add(num[i])
                temp.append(num[i])
                ans(new,temp,ret)
                temp.pop()
            return ret
        return ans(nums,[],[])