class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd = n//2
        even = n//2 if n%2 == 0 else n//2 + 1
        return pow(5,even,10**9+7)*pow(4,odd,10**9+7)% (10**9+7)