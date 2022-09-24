# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], s: int, t: int) -> str:
        def rec(r):
            if not r:
                return [False,False,'']
            right = rec(r.right)
            left = rec(r.left)
            f,l = '',''
            if right[0] and right[1]:
                return right
            if left[0] and left[1]:
                return left
            if right[0]:
                f = right[2]+'U'
            if right[1]:
                l = 'R' + right[2]
            if left[0]:
                f = left[2]+'U'
            if left[1]:
                l = 'L'+left[2]
            val = [right[0] | left[0],right[1] | left[1]]
            if r.val == s:
                val[0] = True
            elif r.val == t:
                val[1] = True
            return [val[0],val[1],f+l]
        return rec(root)[2]