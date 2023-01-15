class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        our goal is to make the total amount of money using a few coin.
        there may be many posibilities of getting that amount of money
        we check every possibilities and we take the one with few coin.
        
        while we are perfoming combination there may be some overlap
        it isn't necessary to solve again again the same problem in order
        not to solve the same problem again again we need to memorize which 
        problem we already solved.
        '''
        memo = {}
        def dp(tot):
            if tot == amount:
                return 0
            if tot > amount:
                return float('inf')
            if tot in memo:
                return memo[tot]
            ans = float('inf')
            for i in coins:
                ans = min(1+dp(tot+i),ans)
            memo[tot] = ans
            return ans
        num_coin = dp(0)
        if num_coin == float('inf'):
            return -1
        return num_coin
        