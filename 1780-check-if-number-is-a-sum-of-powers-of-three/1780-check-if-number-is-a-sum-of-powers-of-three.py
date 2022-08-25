class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        k = int(log(n,3))+1
        dic = {}
        def knapsack(idx,s):
            if s == n:
                return True
            if s>n:
                return False
            if (idx,s) in dic:
                return dic[(idx,s)]
            temp = False
            for i in range(idx,k):
                temp = temp or knapsack(i+1,s+3**i)
            dic[(idx,s)] = temp
            return temp
        return knapsack(0,0)