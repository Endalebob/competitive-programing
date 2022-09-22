class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if not stack or nums[stack[-1]]>nums[i]:
                stack.append(i)
        ans = 0
        i = len(nums)-1
        while stack:
            while stack and nums[stack[-1]]<=nums[i]:
                ans = max(ans,i-stack[-1])
                stack.pop()
            i -= 1
        return ans