class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == '../':
                if stack:
                    stack.pop()
            elif i == './':
                continue
            else:
                stack.append(7)
        return len(stack)