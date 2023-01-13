class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pref = defaultdict(int)
        pref[0] += 1
        ans = 0
        curr = 0
        for i in arr:
            curr += i
            k = curr % 2
            pref[k] += 1
            ans += pref[1-k]
        return ans%(10**9+7)