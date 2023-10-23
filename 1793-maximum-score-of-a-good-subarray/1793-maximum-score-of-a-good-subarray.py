class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = nums[k]
        mi = nums[k]
        l,r = k-1,k+1
        while l>=0 or r<len(nums):
            if l>=0 and r<len(nums):
                if nums[l] < nums[r]:
                    mi = min(mi,nums[r])
                    r += 1
                else:
                    mi = min(mi,nums[l])
                    l -= 1
            elif l>=0:
                mi = min(mi,nums[l])
                l -= 1
            else:
                mi = min(mi,nums[r])
                r += 1
            ans = max(ans,(r-l-1)*mi)
        return ans