class Solution:
    def sol(self, i, j, values, dp):
        if i == j:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        max_val = float('-inf')
        for k in range(i, j):
            curr_val = 0
            if i-1 < 0:
                curr_val = values[k] * values[j] + self.sol(i, k, values, dp) + self.sol(k+1, j, values, dp)
            else:
                curr_val = values[i-1] * values[k] * values[j] + self.sol(i, k, values, dp) + self.sol(k+1, j, values, dp)
            max_val = max(max_val, curr_val)
        
        dp[i][j] = max_val
        return dp[i][j]
    
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        dp = [[-1 for _ in range(n+2)] for _ in range(n+2)]
        return self.sol(0, n, nums, dp)