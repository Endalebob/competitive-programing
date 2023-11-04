class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ants = [0]*(1+n)
        for i in left:
            ants[i] = -1
        for i in right:
            ants[i] = 1
        ans = 0
        for i in range(n+1):
            if ants[i] == 1:
                ans = max(ans,n-i)
            elif ants[i] == -1:
                ans = max(ans,i)
        return ans