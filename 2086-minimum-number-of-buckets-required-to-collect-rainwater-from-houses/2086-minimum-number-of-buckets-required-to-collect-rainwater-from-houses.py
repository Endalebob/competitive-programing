class Solution:
    def minimumBuckets(self, nums: str) -> int:
        dp = [0]*len(nums)
        for i in range(len(nums)):
            flag = False
            if nums[i] == 'H':
                flag = True
                if i<len(nums)-1 and nums[i+1] == '.':
                    flag = False
                    if dp[i-1] == 0:
                        dp[i+1] = 1
                        continue
                if i>0 and nums[i-1] == '.':
                    flag = False
                    dp[i-1] = 1
            if flag:
                return -1
        ans = sum(dp)
        return ans