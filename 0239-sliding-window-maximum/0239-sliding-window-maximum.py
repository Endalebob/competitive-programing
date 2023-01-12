class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sliding_sum = deque()
        for i in range(k):
            while sliding_sum and nums[sliding_sum[-1]] <= nums[i]:
                sliding_sum.pop()
            sliding_sum.append(i)
        ans = [nums[sliding_sum[0]]]
        for i in range(k,len(nums)):
            if sliding_sum[0] <= i-k:
                sliding_sum.popleft()
            while sliding_sum and nums[sliding_sum[-1]] <= nums[i]:
                sliding_sum.pop()
                
            sliding_sum.append(i)
            ans.append(nums[sliding_sum[0]])
        return ans
        