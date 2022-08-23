# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        if not root:
            return 0
        def rec(r):
            left = 1+rec(r.left) if r.left else 0
            right = 1+rec(r.right) if r.right else 0
            cmp = 0
            ret = 0
            if r.left and r.left.val == r.val:
                cmp += left
                ret = max(ret,left)
            if r.right and r.right.val == r.val:
                cmp += right
                ret = max(ret,right)
            self.ans = max(self.ans,cmp)
            return ret
        rec(root)
        return self.ans
            