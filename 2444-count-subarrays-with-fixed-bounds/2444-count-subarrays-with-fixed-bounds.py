class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        out = min_idx = max_idx = -1
        ans = 0
        for i in range(len(nums)):
            if minK > nums[i] or nums[i] > maxK:
                out = i
            if nums[i] == minK:
                min_idx =i
            if nums[i] == maxK:
                max_idx = i
            min_val = min(max_idx,min_idx)
            if min_val > out:
                ans += min_val - out
        return ans