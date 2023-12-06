# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        def dfs(root):
            if not root:
                return 0
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))
            self.ans = max(self.ans,right+left+root.val)
            return max(right,left)+root.val
        dfs(root)
        return self.ans