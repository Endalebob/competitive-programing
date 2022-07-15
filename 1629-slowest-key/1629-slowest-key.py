class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        init = 0
        curr = 0
        ans = ''
        for i in range(len(releaseTimes)):
            if releaseTimes[i]-init>curr:
                curr = releaseTimes[i]-init
                ans = keysPressed[i]
            elif releaseTimes[i]-init == curr:
                ans = max(ans,keysPressed[i])
            init = releaseTimes[i]
        return ans