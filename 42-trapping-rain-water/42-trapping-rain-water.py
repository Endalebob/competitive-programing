from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        deq = deque()
        rdeq = deque()
        deq.append(height[0])
        for i in range(len(height)-1):
            if len(deq)>0 and deq[0]<=height[1+i]:
                ans += (len(deq)*deq[0]-sum(deq))
                deq = deque()
            deq.append(height[i+1])
        deq = list(deq)
        deq = deq[::-1]
        rdeq.append(deq[0])
        for i in range(len(deq)-1):
            if len(rdeq)>0 and rdeq[0]<=deq[1+i]:
                ans += (len(rdeq)*rdeq[0]-sum(rdeq))
                rdeq = deque()
            rdeq.append(deq[i+1])
        return ans
            