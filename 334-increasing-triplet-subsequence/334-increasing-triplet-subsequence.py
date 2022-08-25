class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
                elif nums[i] == nums[j]:
                    dp[i] = max(dp[i],dp[j])
                    break
            if dp[i] == 3:
                return True
        return False