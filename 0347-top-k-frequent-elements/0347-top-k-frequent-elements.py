class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        dic = {}
        heap = []
        for i in count:
            heapq.heappush(heap,[-1*count[i],i])
            
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans