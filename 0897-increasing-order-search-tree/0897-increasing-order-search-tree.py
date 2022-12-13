# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        val = []
        def inord(root):
            if not root:
                return
            inord(root.left)
            val.append(root.val)
            inord(root.right)
        inord(root)
        temp = root = TreeNode()
        for i in val:
            root.right = TreeNode(i)
            root = root.right
        return temp.right