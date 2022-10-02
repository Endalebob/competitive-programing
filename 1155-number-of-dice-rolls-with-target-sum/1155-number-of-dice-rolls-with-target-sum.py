class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def rec(n,sum_):
            if n == 0 and sum_ == target:
                return 1
            if n <= 0 or n*k < target-sum_ or n*1 > target-sum_:
                return 0
            ans = 0
            for i in range(1,k+1):
                ans += rec(n-1,sum_+i)
            return ans
        return rec(n,0)%(10**9+7)
                