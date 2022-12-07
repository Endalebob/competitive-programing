# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            a = root
            left = 0
            right = 0
            while a := a.left:
                left += 1
            a = root
            while a := a.right:
                right += 1
                
            if left == right:
                return 2**(left+1)-1
            else:
                return dfs(root.left) + dfs(root.right) + 1
        return dfs(root)