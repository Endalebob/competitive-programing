class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ans = 1
        unique = set()
        deq = deque()
        for i in rolls:
            prev = len(unique)
            unique.add(i)
            if prev < len(unique):
                deq.append(i)
                if len(deq) == k:
                    ans += 1
                    unique = set()
                    deq = deque()
        return ans