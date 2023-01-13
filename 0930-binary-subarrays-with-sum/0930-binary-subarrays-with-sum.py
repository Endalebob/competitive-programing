class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref_sum = defaultdict(int)
        pref_sum[0] += 1
        ans = 0
        curr = 0
        for i in nums:
            curr += i
            ans += pref_sum[curr-goal]
            pref_sum[curr] += 1
        return ans
            
        