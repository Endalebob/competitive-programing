from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        check = deque()
        for i in s:
            if i in check:
                ans = max(ans,len(check))
                while i in check:
                    check.popleft()
            check.append(i)
        return max(ans,len(check))
        