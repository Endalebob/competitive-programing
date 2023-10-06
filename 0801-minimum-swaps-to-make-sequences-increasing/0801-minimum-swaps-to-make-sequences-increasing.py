class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dp(idx,pr1,pr2):
            if idx == len(nums1):
                return 0
            ans = float('inf')
            if nums1[idx] > pr1 and nums2[idx]>pr2:
                ans = min(ans,dp(idx+1,nums1[idx],nums2[idx]))
            if nums1[idx] > pr2 and nums2[idx] > pr1:
                ans = min(ans,dp(idx+1,nums2[idx],nums1[idx])+1)
            return ans
        return min(dp(1,nums1[0],nums2[0]),dp(1,nums2[0],nums1[0])+1)

        