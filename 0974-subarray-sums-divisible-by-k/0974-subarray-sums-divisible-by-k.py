class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_sum = defaultdict(int)
        pref_sum[0] += 1
        ans = 0
        curr = 0
        for i in nums:
            curr += i
            ans += pref_sum[curr%k]
            pref_sum[curr%k] += 1
        return ans