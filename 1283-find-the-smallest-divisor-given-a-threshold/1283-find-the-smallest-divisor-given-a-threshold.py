import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        left = 1
        right = nums[-1]
        mid = (left + right)//2
        ans = nums[-1]
        while left<right:
            summ = 0
            m = 0
            mid = (left + right)//2
            while summ<=threshold and m<=len(nums)-1:
                summ += (math.ceil(nums[m]/mid))
                m += 1
            if summ<=threshold:
                ans = mid
                right = mid
            else:
                left = mid +1
        return ans
                
            