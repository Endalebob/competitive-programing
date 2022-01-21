class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(heights)):
            m = 0
            ans = max(ans, heights[i])
            while len(stack)>0 and stack[-1][1]>heights[i]:
                if len(stack)>1:
                    ans = max(ans, ((i-1)-stack[-2][0])*stack[-1][1])
                else:
                    ans = max(ans, stack[-1][1]*i)
                stack.pop()
                m   += 1
            stack.append([i,heights[i]])
        for i in range(1,len(stack)):
            wid = (len(heights)-1)-stack[-i-1][0]
            ans = max(ans,wid*stack[-i][1])
        ans = max(ans, stack[0][1]*len(heights))
        return ans