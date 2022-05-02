class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [-1] + [i for i in range(len(nums)) if nums[i] % 2 == 1] + [len(nums)]
        ans = 0
        for i in range(k,len(odds)-1):
            start = odds[i-k+1]-odds[i-k]
            end = odds[i+1] -odds[i]
            ans += end*start
        return ans
       