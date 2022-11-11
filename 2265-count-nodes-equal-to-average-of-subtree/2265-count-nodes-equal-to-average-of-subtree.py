# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        def dfs(root):
            if not root:
                return 0,0
            su_ml,numl = dfs(root.left)
            su_mr,numr = dfs(root.right)
            total = su_ml+su_mr + root.val
            total_num = numl+numr+1
            if root.val == total//total_num:
                self.answer += 1
            return total,total_num
        dfs(root)
        return self.answer