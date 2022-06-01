# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dls(node,depthlimit):
            if not node.left and not node.right:
                return True
            if depthlimit <= 0:
                return False
            if node.left:
                if dls(node.left,depthlimit-1):
                    return True
            if node.right:
                if dls(node.right,depthlimit-1):
                    return True
        def iddfs(maxdepth):
            if not root.left and not root.right:
                return 1
            for i in range(maxdepth):
                if dls(root,i+1):
                    return i+2
        return iddfs(100000)
                
                    