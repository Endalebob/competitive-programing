# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(r,s):
            if not r:
                return 0
            if not r.left and not r.right:
                return int(s+str(r.val))
            return dfs(r.left,s+str(r.val)) + dfs(r.right,s+str(r.val))
        return dfs(root,'')