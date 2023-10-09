# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0,-10000
            l = dfs(node.left)
            r = dfs(node.right)
            left = max(0,l[0])
            right = max(0,r[0])
            return max(left,right)+node.val, max(left+right+node.val,l[1],r[1])
        return dfs(root)[1]
        