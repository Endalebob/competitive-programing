class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0]*len(heights)
        popped = [1]*len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                ans[stack[-1]] += popped[i]
                popped[i] = popped[stack.pop()] +1
            stack.append(i)
        for i in range(len(stack)-2,-1,-1):
            ans[stack[i]] += popped[stack[i+1]]
        return ans