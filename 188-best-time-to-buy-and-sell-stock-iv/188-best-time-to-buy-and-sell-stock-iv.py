class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def rec(b_or_s,k,idx):
            if k<1 or idx>=len(prices):
                return 0
            if b_or_s == 0:
                return max(rec(b_or_s,k,idx+1),rec(1-b_or_s,k,idx+1)-prices[idx])
            return max(rec(b_or_s,k,idx+1),rec(1-b_or_s,k-1,idx+1)+prices[idx])
        return rec(0,k,0)