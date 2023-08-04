# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(root):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)
            mid = (root == p) or (root == q)
            tot = left + right + mid
            if tot>1:
                self.ans = root
            return tot>0
        dfs(root)
        return self.ans