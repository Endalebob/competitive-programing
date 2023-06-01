class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        val = defaultdict(int)
        ans = 1
        for i in arr:
            val[i] = val[i-diff]+1
            ans = max(ans,val[i])
        return ans