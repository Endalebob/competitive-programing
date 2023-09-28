class Solution:
    def isValid(self, s: str) -> bool:
        open_par = {')':'(','}':'{',']':'['}
        idx = 0
        stack = []
        while idx < len(s):
            if s[idx] in open_par:
                if stack and stack[-1] == open_par[s[idx]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[idx])
            idx += 1
        return len(stack) == 0