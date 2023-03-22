class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = ''
        for i in range(1,n+1):
            s += str(i)
        return ''.join(list(permutations(s,n))[k-1])
        