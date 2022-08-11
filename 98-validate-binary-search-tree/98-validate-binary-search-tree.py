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
        for i in range(len(ans)-1):
            if ans[i+1]<=ans[i]:
                return False
        return True