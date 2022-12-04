class Solution:
    def countArrangement(self, n: int) -> int:
        nums = list(range(1,n+1))
        def dfs(idx):
            if idx == n+1:
                return 1
            ans = 0
            for i in range(len(nums)):
                if nums[i] % idx == 0 or idx % nums[i] == 0:
                    temp = nums[i]
                    nums[i] = 31
                    ans += dfs(idx+1)
                    nums[i] = temp
            return ans
        return dfs(1)