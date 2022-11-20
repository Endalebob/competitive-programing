class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr = 0
        dic = {}
        ans = 0
        for i in range(len(nums)):
            curr = curr+1 if nums[i] else curr-1
            if 0 == curr:
                ans = i+1
            elif curr not in dic:
                dic[curr] = i
            else:
                ans = max(ans,i-dic[curr])
        return ans