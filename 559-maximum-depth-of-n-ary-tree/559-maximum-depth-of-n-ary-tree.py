"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.answer = 0
        def dfs(root,level):
            self.answer = max(self.answer,level)
            for child in root.children:
                dfs(child,level+1)
        dfs(root,1)
        return self.answer