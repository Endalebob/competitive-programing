# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        dummy = TreeNode()
        dummy.left = root
        def dfs(root):
            if not root:
                return 0
            r,l = dfs(root.right),dfs(root.left)
            if r == 1 and root.right.val == target:
                r = 0
                root.right = None
            if l == 1 and root.left.val == target:
                l = 0
                root.left = None
                
            return r+l+1
        dfs(dummy)
        return dummy.left