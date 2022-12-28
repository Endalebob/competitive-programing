class Solution:
    def maxJump(self, s: List[int]) -> int:
        ans = s[-1]-s[0]
        ret = -float('inf')
        for i in range(0,len(s)-2,2):
            ret = max(s[i+2]-s[i],ret)
        for i in range(1,len(s)-2,2):
            ret = max(s[i+2]-s[i],ret)
        if len(s) > 2:
            ret = max(ret,s[1]-s[0],s[-1]-s[-2])
        else:
            ret = s[-1]-s[0]
        return min(ans,ret)