class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][-1] == '(' and s[i] == ')': stack.pop()
            else: stack.append([i,s[i]])
        if not stack:
            return len(s)
        ans = stack[0][0]
        for i in range(len(stack)-1):
            ans = max(ans,stack[i+1][0]-stack[i][0]-1)
            
        return max(ans,len(s)-stack[-1][0]-1)