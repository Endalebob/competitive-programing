class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr)-1:
            return max(arr)
        pos_0 = 0
        deq = deque(arr)
        while 1:
            while pos_0 < k and deq[0] > deq[1]:
                deq[0],deq[1] = deq[1],deq[0]
                deq.append(deq[0])
                deq.popleft()
                pos_0 += 1
            if pos_0 >= k:
                return deq[0]
            deq.append(deq[0])
            deq.popleft()
            pos_0 = 1