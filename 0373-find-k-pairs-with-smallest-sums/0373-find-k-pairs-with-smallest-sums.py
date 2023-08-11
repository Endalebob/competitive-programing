class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        vstd = set()
        heapq.heappush(heap,(nums1[0]+nums2[0],0,0))
        ans = []
        while k and heap:
            val,i1,i2 = heapq.heappop(heap)
            ans.append([nums1[i1],nums2[i2]])
            if i1+1 < len(nums1) and (i1+1,i2) not in vstd:
                vstd.add((i1+1,i2))
                heapq.heappush(heap,(nums1[i1+1]+nums2[i2],i1+1,i2))
            if i2+1 < len(nums2) and (i1,i2+1) not in vstd:
                vstd.add((i1,i2+1))
                heapq.heappush(heap,(nums1[i1]+nums2[i2+1],i1,i2+1))
            k -= 1
        return ans
        
        