# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ret = -1000
        def rec(r):
            right,left = 0,0
            if r.left:
                left = rec(r.left)
                left += r.left.val
            if r.right:
                right = rec(r.right)
                right += r.right.val
            if right>0 and left>0:
                self.ret = max(self.ret,left+right+r.val)
            elif right>0:
                self.ret = max(self.ret,right+r.val)
            elif left>0:
                self.ret = max(self.ret,left+r.val)
            else:
                self.ret = max(self.ret,r.val)
            return max(left,right,0)
        rec(root)
        return self.ret
                