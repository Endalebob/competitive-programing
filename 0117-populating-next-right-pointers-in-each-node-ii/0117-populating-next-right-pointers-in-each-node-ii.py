"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        deq = deque([root])
        while deq:
            temp = []
            for i in range(len(deq)-1):
                if deq[i].left:
                    temp.append(deq[i].left)
                if deq[i].right:
                    temp.append(deq[i].right)
                deq[i].next = deq[i+1]
            if deq[-1].left:
                temp.append(deq[-1].left)
            if deq[-1].right:
                temp.append(deq[-1].right)
            deq = temp
        return root