"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        deq = deque()
        deq.append(root)
        ret = []
        while deq:
            temp = []
            for i in range(len(deq)):
                a = deq.popleft()
                if a:
                    temp.append(a.val)
                    for j in a.children:
                        deq.append(j)
            if temp:
                ret.append(temp)
        return ret
    
                