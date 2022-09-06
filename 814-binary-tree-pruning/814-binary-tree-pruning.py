# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(r):
            flag = False
            if r.left:
                check = dfs(r.left)
                if not check:
                    r.left = None
                flag = flag or check
            if r.right:
                check = dfs(r.right)
                if not check:
                    r.right = None
                flag = flag or check
            return (r.val == 1) or flag
        if not dfs(root):
            return None
        return root
               