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
        memo = {amount:0}
        for tot in range(amount-1,-1,-1):
            cur = float('inf')
            for i in coins:
                if tot + i in memo:
                    cur = min(cur,memo[tot+i]+ 1)
            memo[tot] = cur
        if memo[0] == float('inf'):
            return -1
        return memo[0]
        