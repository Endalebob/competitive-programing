class Solution:
    def minimumDeletions(self, s: str) -> int:
        pre_sum = [0]*(len(s)+1)
        prev = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == 'a':
                prev += 1
            pre_sum[i] = prev
        ans = pre_sum[0]
        curr=0
        ret = 0
        for i in range(len(s)):
            
            ans = min(ans,pre_sum[i]+curr)
            if s[i] == 'b':
                curr += 1
        ans = min(ans,pre_sum[-1]+curr)
        return ans