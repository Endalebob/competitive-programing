import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
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
        
        # unique = set(nums)
        # dic = {}
        # for i in unique:
        #     dic[i] = nums.count(i)
        # nwv = list(dic.values())
        # nwk = list(dic.keys())
        # check = nwv[:]
        # check.sort()
        # print(nwk)
        # print(nwv)
        # print(check)
        # ld = []
        # for i in range(k):
        #     m = nwv.index(check[-1-i])
        #     nwv[m] = 0
        #     print(m)
        #     ld.append(nwk[m])
        # return ld  