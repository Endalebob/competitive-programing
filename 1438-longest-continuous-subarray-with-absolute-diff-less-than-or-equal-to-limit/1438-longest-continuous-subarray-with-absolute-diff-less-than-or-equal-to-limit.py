from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()
        left = 0
        ans = 0
        for i,v in enumerate(nums):
            while inc and inc[-1][1]>v:
                inc.pop()
            while dec and dec[-1][1]<v:
                dec.pop()
            inc.append([i,v])
            dec.append([i,v])
            while (dec[0][1] - inc[0][1]) > limit:
                if inc[0][0] <= left:
                    inc.popleft()
                if dec[0][0] <= left:
                    dec.popleft()
                left += 1
            c = max(inc[-1][0], dec[-1][0])
            ans = max(ans,i-left+1)
      
        return ans