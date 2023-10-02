class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if stack:
                if stack[-1][0] == i:
                    stack[-1][1] += 1
                else:
                    stack.append([i,1])
            else:
                stack.append([i,1])
            if stack[-1][1] == k:
                stack.pop()
        ans = ''
        for i,j in stack:
            ans += i*j
        return ans