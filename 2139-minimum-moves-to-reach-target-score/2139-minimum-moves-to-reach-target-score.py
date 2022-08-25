class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = -1
        t = 0
        for i in range(maxDoubles):
            if target == 1:
                break
            t += 1
            ans += target%2
            target //= 2
        ans += target
        return ans+t