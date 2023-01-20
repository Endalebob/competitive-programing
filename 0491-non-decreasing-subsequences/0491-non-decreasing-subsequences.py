class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dp(idx,temp):
            if len(temp) > 1:
                ans.append(temp.copy())
            if idx == len(nums):
                return
            vstd = set()
            for i in range(idx,len(nums)):
                if nums[i] not in vstd:
                    if temp and temp[-1] > nums[i]:
                        continue
                    vstd.add(nums[i])
                    temp.append(nums[i])
                    dp(i+1,temp)
                    temp.pop()
            return ans
        return dp(0,[])