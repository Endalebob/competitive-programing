
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def ans(num,temp,ret):
            if not num:
                ret.append(deepcopy(temp))
            for i in range(len(num)):
                new = num[:i]+num[i+1:]
                temp.append(num[i])
                ans(new,temp,ret)
                temp.pop()
            return ret
        return ans(nums,[],[])