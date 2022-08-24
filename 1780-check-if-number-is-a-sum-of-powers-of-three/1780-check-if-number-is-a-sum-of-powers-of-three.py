class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        k = int(log(n,3))+1
        @cache
        def knapsack(idx,s):
            if s == n:
                return True
            if s>n:
                return False
            temp = False
            for i in range(idx,k):
                temp = temp or knapsack(i+1,s+3**i)
            return temp
        return knapsack(0,0)