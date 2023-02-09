class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        s, l, r = 0, 0, 0
        wl, wr = {}, {}
        res = 0
        while l < len(nums):
            while l < len(nums) and len(wl) < k:
                if nums[l] not in wl:
                    wl[nums[l]] = 0
                wl[nums[l]] += 1
                l += 1
            if len(wl) < k:
                return res
            while r < len(nums) and len(wr) <= k:
                if nums[r] not in wr:
                    wr[nums[r]] = 0
                wr[nums[r]] += 1
                r += 1
            if r == len(nums) and len(wr) == k:
                r += 1
            while s < l and len(wl) == k:
                res += r - l
                wl[nums[s]] -= 1
                if not wl[nums[s]]:
                    wl.pop(nums[s])
                wr[nums[s]] -= 1
                if not wr[nums[s]]:
                    wr.pop(nums[s])
                s += 1
        return res
