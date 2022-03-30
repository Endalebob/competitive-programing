# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            right_sum = dfs(root.right)
            left_sum = dfs(root.left)
            self.ans += (max(right_sum,left_sum)-min(right_sum,left_sum))
            return right_sum +left_sum + root.val
        self.ans = 0
        dfs(root)
        return self.ans