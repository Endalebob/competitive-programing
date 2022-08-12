# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val = []
        def rec(node):
            if not node:
                return []
            ans = []
            if node == p or node == q:
                ans = [node]
            ans = rec(node.left) + ans + rec(node.right)
            if len(ans) == 2 and not val:
                val.append(node)
            return ans
        rec(root)
        return val[0]
        