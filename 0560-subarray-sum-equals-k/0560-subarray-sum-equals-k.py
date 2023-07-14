class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = defaultdict(int)
        pref_sum[0] += 1
        curr = 0
        ans = 0
        for i in nums:
            curr += i
            ans += pref_sum[curr-k]
            pref_sum[curr] += 1
        return ans