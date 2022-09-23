class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join([format(i,'b') for i in range(n+1)]),2) %(10**9+7)