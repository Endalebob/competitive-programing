class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        first consider I conver every zero in to one.
        '''
        m = 0
        for i in s:
            if i == '0':
                m += 1
        ans = m
        for i in s:
            if i == '0':
                m -= 1
                ans = min(m,ans)
            else:
                m += 1
        return ans