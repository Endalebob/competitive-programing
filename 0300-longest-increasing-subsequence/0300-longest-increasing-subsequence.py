class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for i in nums:
            if i > ans[-1]:
                ans.append(i)
            else:
                ans[bisect_left(ans,i)] = i
                
        return len(ans)
            