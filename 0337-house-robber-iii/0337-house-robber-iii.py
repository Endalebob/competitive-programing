# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(root,flag):
            if not root:
                return 0
            if (root,flag) in memo:
                return memo[(root,flag)]
            if flag:
                memo[(root,flag)]=max(root.val+dp(root.left,1-flag)+dp(root.right,1-flag),dp(root.left,flag)+dp(root.right,flag))
            else: memo[(root,flag)]= dp(root.left,1-flag)+dp(root.right,1-flag)
            return memo[(root,flag)]
        return dp(root,1)