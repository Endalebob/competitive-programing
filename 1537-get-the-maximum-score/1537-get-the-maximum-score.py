class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        map1,map2 = {},{}
        for i,v in enumerate(nums1):
            map1[v] = i
        for i,v in enumerate(nums2):
            map2[v] = i
        @lru_cache(None)
        def dp(turn,idx):
            if turn == 1 and idx == len(nums1):
                return 0
            if turn == 2 and idx == len(nums2):
                return 0
            ans = 0
            if turn == 1:
                ans = dp(turn,idx+1)+nums1[idx]
                if nums1[idx] in map2:
                    ans = max(ans,dp(3-turn,map2[nums1[idx]]+1)+nums2[map2[nums1[idx]]])
            else:
                ans = dp(turn,idx+1)+nums2[idx]
                if nums2[idx] in map1:
                    ans = max(ans,dp(3-turn,map1[nums2[idx]]+1)+nums1[map1[nums2[idx]]])
            return ans
        return max(dp(1,0),dp(2,0))%(10**9+7)
            