import heapq
class Solution:
    def topKFrequent(self, nums: List[str], k: int) -> List[str]:
        dic = {}
        nums.sort()
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        frequency = list(dic.values())
        numbers = list(dic.keys())
        heaplist = [-i for i in frequency]
        heapq.heapify(heaplist)
        ans = []
        for i in range(k):
            j = frequency.index(-1*heapq.heappop(heaplist))
            frequency[j] = 0
            ans.append(numbers[j])
        return ans