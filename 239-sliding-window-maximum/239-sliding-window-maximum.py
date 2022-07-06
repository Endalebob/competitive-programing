from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        ans = []
        for i in range(k):
            while deq and nums[deq[-1]]<=nums[i]:
                deq.pop()
            deq.append(i)
        ans.append(nums[deq[0]])
        left = k
        while left<len(nums):
            while len(deq)>=k:
                deq.popleft()
            if deq and deq[0]+k <= left:
                deq.popleft()
            while deq and nums[deq[-1]]<=nums[left]:
                deq.pop()
            deq.append(left)
            ans.append(nums[deq[0]])
            left += 1
        return ans