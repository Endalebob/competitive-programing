# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root,ma_x,mi_n):
            
            #base case
            if not root: return 0
            
            #max difference from right node 
            left = dfs(root.left,max(ma_x,root.val),min(mi_n,root.val))
            
            #max dfference from left node
            right = dfs(root.right,max(ma_x,root.val),min(mi_n,root.val))
            
            #retrun maximum of right,left and difference of current node with ancestor
            return max(left,right,abs(ma_x-root.val),abs(mi_n-root.val))
        
        return dfs(root,root.val,root.val)