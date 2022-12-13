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
        root = temp = TreeNode()
        for i in range(len(val)-1):
            root.val = val[i]
            root.right = TreeNode()
            root = root.right
        root.val = val[-1]
        return temp