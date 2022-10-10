# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.updated_value = 0
        def dfs(r):
            if not r:
                return None
            node = dfs(r.right)
            self.updated_value += r.val
            r.val = self.updated_value
            dfs(r.left)
            return r
        dfs(root)
        return root
        