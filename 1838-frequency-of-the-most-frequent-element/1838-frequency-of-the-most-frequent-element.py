from collections import deque
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        deq = deque()
        ans = 1
        nums.sort()
        differ = 0
        for i in nums:
            deq.append(i)
            if len(deq)>1:
                differ = (deq[-1] - deq[-2])*(len(deq)-1)+differ
            while len(deq)>1 and differ>k:
                differ -= i - deq.popleft()
            if len(deq)>ans:
                ans = len(deq)
        return ans
            