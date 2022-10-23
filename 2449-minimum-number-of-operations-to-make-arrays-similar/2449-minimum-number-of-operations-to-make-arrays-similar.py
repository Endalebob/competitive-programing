class Solution:
    def makeSimilar(self, a: List[int], b: List[int]) -> int:
        a.sort(key = lambda x:[x%2,x])
        b.sort(key = lambda x:[x%2,x])
        ans = sum([abs(a[i]-b[i]) for i in range(len(a))])
        return ans//4
        