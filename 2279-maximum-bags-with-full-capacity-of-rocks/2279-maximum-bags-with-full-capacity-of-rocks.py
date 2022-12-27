class Solution:
    def maximumBags(self, c: List[int], r: List[int], a: int) -> int:
        heap = []
        for i in range(len(c)):
            if c[i]-r[i] > 0:
                heap.append(c[i]-r[i])
        heap.sort()
        for i in range(1,len(heap)):
            heap[i] += heap[i-1]
        idx = bisect_right(heap,a)
        return len(c)-len(heap)+idx