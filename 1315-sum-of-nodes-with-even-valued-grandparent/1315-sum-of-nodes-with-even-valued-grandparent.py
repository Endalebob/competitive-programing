# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root,a,b):
            if not root:
                return 0
            if a % 2 == 0:
                self.ans += root.val
            a = b
            b = root.val
            right = dfs(root.right,a,b)
            left = dfs(root.left,a,b)
        self.ans = 0
        dfs(root,1,1)
        return self.ans
        