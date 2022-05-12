class Solution:
    def countTriples(self, n: int) -> int:
        nItems = set()
        for i in range(n):
            nItems.add(float(i+1))
        ans = 0
        for i in range(1,n+1):
            for j in range(i+1,n):
                sumSq = i**2 + j**2
                sqrt = sumSq ** 0.5
                if sqrt in nItems:
                    ans += 1
        return ans*2