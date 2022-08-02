class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic = {}
        def dp(am):
            if am == 0:
                return 0
            if am in dic:
                return dic[am]
            ans = float('inf')
            for i in coins:
                if am-i>=0:
                    ans = min(ans,dp(am-i)+1)
            dic[am] = ans
            return ans
        ans = dp(amount)
        if ans > amount:
            return -1
        return ans