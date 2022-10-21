class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r,l = 0,0
        check = set()
        while r<len(nums):
            check.add(nums[r])
            if len(check) <= r-l:
                return True
            if r - l >= k:
                check.remove(nums[l])
                l += 1
            r += 1
        return False