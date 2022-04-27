from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre_sum = [0]*(len(nums)+1)
        for i,v in enumerate(nums):
            pre_sum[i+1] = pre_sum[i] + v
        deq = deque()
        ans = len(nums) + 1
        for i in range(len(pre_sum)):
            while deq and pre_sum[i] - pre_sum[deq[0]] >= k:
                ans = min(ans,i-deq.popleft())
            while deq and pre_sum[i] < pre_sum[deq[-1]]:
                deq.pop()
            deq.append(i)
        if ans == len(nums)+1:
            return -1
        return ans
        
                