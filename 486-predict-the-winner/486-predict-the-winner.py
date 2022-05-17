class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        dp = [num for num in nums]
        for length in range(2, len(nums) + 1):
            new_dp = []
            for j in range(len(nums) - length + 1):
                new_dp.append(max(nums[j] - dp[j + 1], nums[j + length - 1] - dp[j]))
            dp = new_dp[:]
        return dp[0] >= 0