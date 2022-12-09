# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root,ma_x,mi_n):
            
            if not root: return 0
            left = dfs(root.left,max(ma_x,root.val),min(mi_n,root.val))
            right = dfs(root.right,max(ma_x,root.val),min(mi_n,root.val))
            return max(left,right,abs(ma_x-root.val),abs(mi_n-root.val))
        
        return dfs(root,root.val,root.val)