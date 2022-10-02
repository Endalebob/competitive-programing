class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def rec(num,s):
            if num == 0 and s == target:
                return 1
            if num <= 0 or num*k < target-s or num*1 > target-s:
                return 0
            ans = 0
            for i in range(1,k+1):
                ans += rec(num-1,s+i)
            return ans
        return rec(n,0)%(10**9+7)
                