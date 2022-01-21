from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped = deque(popped)
        for i in range (len(pushed)):
            stack.append(pushed[i])
            while len(stack) != 0 and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()
        return len(popped) == 0
            
            

                 
                