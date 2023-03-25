class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = defaultdict(int)
        pref[0] += 1
        curr = 0
        ans = 0
        for i in nums:
            curr += i
            ans += pref[curr-goal]
            pref[curr] += 1
        return ans