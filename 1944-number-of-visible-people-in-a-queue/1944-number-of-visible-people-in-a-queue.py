class Solution:
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
                if stack:
                    answer[stack[-1]] += 1
            stack.append(i)
        answer[-1] = 0
        return answer