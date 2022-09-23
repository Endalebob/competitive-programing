class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        val = []
        heapq.heapify(val)
        heapq.heappush(val,(nums1[0]+nums2[0],0,0))
        ans = []
        vstd = set()
        while len(ans)<k and val:
            curr = heapq.heappop(val)
            if len(nums1)>curr[1]+1:
                if (curr[1]+1,curr[2]) not in vstd:
                    vstd.add((curr[1]+1,curr[2]))
                    heapq.heappush(val,(nums1[curr[1]+1]+nums2[curr[2]],curr[1]+1,curr[2]))
            if len(nums2)>curr[2]+1:
                if (curr[1],curr[2]+1) not in vstd:
                    vstd.add((curr[1],curr[2]+1))
                    heapq.heappush(val,(nums1[curr[1]]+nums2[curr[2]+1],curr[1],curr[2]+1))
            ans.append([nums1[curr[1]],nums2[curr[2]]])
        return ans
            