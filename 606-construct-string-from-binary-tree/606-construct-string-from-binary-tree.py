# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(r):
            if not r:
                return ''
            ans = '('+str(r.val)
            left = dfs(r.left)
            right = dfs(r.right)
            if not left and right:
                left = '()'
            return ans+left+right+')'
        return dfs(root)[1:-1]