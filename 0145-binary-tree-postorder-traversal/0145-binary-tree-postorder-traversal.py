# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def pot(root,val):
            if not root:
                return
            pot(root.left,val)
            pot(root.right,val)
            val.append(root.val)
        va = []
        pot(root,va)
        return va