class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        mp = {}
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
        ans = 1
        for i in range(n):
            for j in range(i + 1, n):
                d = nums[j] - nums[i]
                k = nums[j] - 2 * d 
                if k in mp:
                    pos = mp[k]
                    dp[i][j] = max(dp[i][j], 1 + dp[pos][i])
                else:
                    dp[i][j] = 2
                ans = max(ans, dp[i][j])
            mp[nums[i]] = i
        return ans
