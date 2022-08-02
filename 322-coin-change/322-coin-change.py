class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        val = [0]*(amount+1)
        for i in range(1,amount+1):
            val[i] = float('inf')
            for j in coins:
                if i-j>=0:
                    val[i] = min(val[i],val[i-j]+1)
        return val[amount] if val[amount]<=amount else -1