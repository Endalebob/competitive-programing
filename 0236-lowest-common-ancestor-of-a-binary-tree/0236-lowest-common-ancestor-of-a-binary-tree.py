# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return [False,False,-1]
            left = dfs(root.left)
            right = dfs(root.right)
            if left[0] and left[1]:
                return left
            if right[0] and right[1]:
                return right
            return [(left[0] or right[0] or (root.val == p.val)),(left[1] or right[1] or (root.val == q.val)),root]
        return dfs(root)[2]