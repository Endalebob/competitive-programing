# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root,depth):
            if root.left and root.right:
                return max(dfs(root.left,2*depth),dfs(root.right,2*depth + 1))
            elif root.left:
                return (dfs(root.left,2*depth))
            return depth
        return dfs(root,1)
            