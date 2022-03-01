"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        depth = 1
        ans = depth
        for child in root.children:
            ans= max(ans,self.dfs(child,depth))
        return ans
    def dfs(self,root,depth):
        depth += 1
        ans = depth
        for child in root.children:
            ans= max(ans,self.dfs(child,depth))
        return ans

            
            
            