class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pref_ = [nums[0]]
        for i in range(1,len(nums)):
            pref_.append(pref_[-1]+nums[i])
        ans = []
        for i in queries:
            ans.append(bisect_right(pref_,i))
        return ans