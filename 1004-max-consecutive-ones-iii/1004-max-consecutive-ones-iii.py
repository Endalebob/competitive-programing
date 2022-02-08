from collections import deque
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        zero = deque()
        holder = 0
        count_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(i)
                count_zero += 1
            if count_zero > k:
                count_zero -= 1
                ans = max(ans,i-holder)
                holder = zero.popleft() + 1
        return max(ans,i+1-holder)