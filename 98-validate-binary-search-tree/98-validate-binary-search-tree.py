# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(ro):
            if not ro: return []
            return valid(ro.left) + [ro.val] + valid(ro.right)
        ans = valid(root)
        return (ans == sorted(ans) and len(ans) == len(set(ans)))