class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        ans = []
        for i in queries:
            ans.append(bisect_right(nums,i))
        return ans