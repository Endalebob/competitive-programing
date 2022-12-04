class Solution:
    def countArrangement(self, n: int) -> int:
        nums = tuple(range(1,n+1))
        @lru_cache(None)
        def dfs(idx,num):
            if idx == n+1:
                return 1
            ans = 0
            for i in range(len(num)):
                if num[i] % idx == 0 or idx % num[i] == 0:
                    # temp = nums[i]
                    # nums[i] = 31
                    new = tuple([j for j in num if j != num[i]])
                    ans += dfs(idx+1,new)
                    # nums[i] = temp
            return ans
        return dfs(1,nums)