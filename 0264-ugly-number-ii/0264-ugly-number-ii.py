class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [2,3,5]
        heap = []
        heapq.heappush(heap,1)
        vstd = set()
        while n:
            curr = heapq.heappop(heap)
            for i in ugly:
                if i*curr not in vstd:
                    vstd.add(i*curr)
                    heapq.heappush(heap,i*curr)
            n -= 1
        return curr