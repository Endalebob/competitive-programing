class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        for i in costs:
            coins -= i
            if coins<0:
                break
            cnt += 1
        return cnt