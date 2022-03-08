# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ans = None
        self.max_depth = 0
        def dfs(root,depth):
            if root:
                left_depth = dfs(root.left,depth+1)
                right_depth = dfs(root.right,depth+1)
                self.max_depth = max(left_depth,right_depth,self.max_depth)
                if self.max_depth == right_depth == left_depth:
                    self.ans = root
                return max(left_depth,right_depth)
            return depth
        dfs(root,0)
        return self.ans