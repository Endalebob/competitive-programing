class Solution:
    def maxConsecutiveAnswers(self, a: str, k: int) -> int:
        tf = [0,0]
        l,r = 0,0
        ans = 1
        while r<len(a):
            while min(tf) > k:
                if a[l] == 'T':
                    tf[0] -= 1
                else:
                    tf[1] -= 1
                l += 1
            ans = max(ans,r-l)
            if a[r] == 'T':
                tf[0] += 1
            else:
                tf[1] += 1
            r += 1
        if min(tf)<=k:
            return max(ans,r-l)
        return max(ans,r-l-1)
                