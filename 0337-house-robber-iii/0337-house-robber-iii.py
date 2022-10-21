# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dp(root,flag):
            if not root:
                return 0
            if flag:
                return max(root.val+dp(root.left,1-flag)+dp(root.right,1-flag),dp(root.left,flag)+dp(root.right,flag))
            return dp(root.left,1-flag)+dp(root.right,1-flag)
        return dp(root,1)