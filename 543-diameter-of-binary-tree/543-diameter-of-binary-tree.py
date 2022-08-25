# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def rec(r):
            if not r:
                return -1
            left = 1+rec(r.left)
            right = 1+rec(r.right)
            self.ans = max(self.ans,left+right)
            return max(left,right)
        rec(root)
        return self.ans
            