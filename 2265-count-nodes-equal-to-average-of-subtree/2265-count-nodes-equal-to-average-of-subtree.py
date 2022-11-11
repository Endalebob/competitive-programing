# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0,0,0
            su_ml,numl,ansl = dfs(root.left)
            su_mr,numr,ansr = dfs(root.right)
            ans = ansl+ansr
            total = su_ml+su_mr + root.val
            total_num = numl+numr+1
            if root.val == total//total_num:
                ans += 1
            return total,total_num,ans
        return dfs(root)[2]