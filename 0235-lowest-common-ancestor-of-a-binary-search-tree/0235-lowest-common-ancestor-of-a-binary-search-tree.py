# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = 0
        def dfs(root):
            if not root:
                return False
            left = dfs(root.left)
            right = dfs(root.right)
            mid = root.val == p.val or root.val == q.val
            if left + right + mid >= 2:
                self.ans = root
            return left or right or mid
        dfs(root)
        return self.ans