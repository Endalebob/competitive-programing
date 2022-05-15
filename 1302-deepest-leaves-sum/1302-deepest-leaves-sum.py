# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.deepest_sum = 0
        def dfs(node,deep):
            if not node.left and not node.right:
                if deep > self.depth:
                    self.deepest_sum = node.val
                elif deep == self.depth:
                    self.deepest_sum += node.val
                self.depth = max(deep,self.depth)
                return self.deepest_sum
            if node.left:
                dfs(node.left,deep+1)
            if node.right:
                dfs(node.right,deep+1)
            return self.deepest_sum
        return dfs(root,0)
        