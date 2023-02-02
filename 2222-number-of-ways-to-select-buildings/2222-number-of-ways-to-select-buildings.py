class Solution:
    def numberOfWays(self, s: str) -> int:
        # @lru_cache(None)
        # def dp(idx,prve):
        #     if idx >= len(s):
        #         return 0
        #     if len(prve) == 3:
        #         return 1
        #     if prve:
        #         if prve[-1] == s[idx]:
        #             return dp(idx+1,prve) + dp(idx+1,s[idx])
        #         return dp(idx+1,prve) + dp(idx+1,s[idx]) + dp(idx+1,prve+s[idx])
        #     return dp(idx+1,s[idx]) + dp(idx+1,prve)
        # return dp(0,'')
        ans = 0
        
        count_of_1 = 0
        count_of_0 = 0
        count_of_10 = 0
        count_of_01 = 0
        for i in s:
            if i == '1':
                count_of_1 += 1
                count_of_01 += count_of_0
                ans += count_of_10
            else:
                count_of_0 += 1
                count_of_10 += count_of_1
                ans += count_of_01
        return ans
            
        