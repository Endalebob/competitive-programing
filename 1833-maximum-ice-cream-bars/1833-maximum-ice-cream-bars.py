class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        '''
        1: I sort the costs because I need to start from low price
        2: I continue until my the sum of visited index is less than
            coins
        3: finally I return the number of visited index
        '''
        costs.sort()
        cnt = 0
        for i in costs:
            coins -= i
            if coins<0:
                break
            cnt += 1
        return cnt