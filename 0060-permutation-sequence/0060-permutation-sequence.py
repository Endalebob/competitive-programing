class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        val = [str(i) for i in range(1,n+1)]
        return ''.join(list(permutations(val,n))[k-1])
        