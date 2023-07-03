class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in dic and (not stack or stack[-1] != dic[i]):
                return False
            if i not in dic:
                stack.append(i)
            else:
                stack.pop()
        return not stack
            