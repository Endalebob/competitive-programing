# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def value(root):
            if not root: return
            if root.val == val: return root
            if root.val > val: return value(root.left)
            return value(root.right)
        return value(root)