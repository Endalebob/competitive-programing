class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(pre,tup):
            if not tup:
                return 1
            vstd = set()
            ans = 0
            for i in range(len(tup)):
                if tup[i] not in vstd:
                    if pre == -1 or (int((pre + tup[i]) ** 0.5))**2 == pre+tup[i]:
                        vstd.add(tup[i])
                        temp = tup[:i] + tup[i+1:]
                        ans += dp(tup[i],tuple(temp))
            return ans
        return dp(-1,tuple(nums))