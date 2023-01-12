class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(heights)
        i = 0
        while i<len(heights):
            while stack and heights[stack[-1]] < heights[i]:
                ans[stack.pop()] += 1
                if stack:
                    ans[stack[-1]] += 1
            stack.append(i)
            i += 1
        for i in range(len(stack)-1):
            ans[stack[i]] += 1
        return ans