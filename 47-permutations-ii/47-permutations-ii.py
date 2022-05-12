class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(num):
            if len(num) == 1:
                return [num]
            val = []
            vstd = set()
            for i in range(len(num)):
                if num[i] in vstd:
                    continue
                kk = num[:i] + num[i+1:]
                temp = dfs(kk)
                vstd.add(num[i])
                for ii in temp:
                    val.append([num[i]]+ii)
            return val
        return dfs(nums)