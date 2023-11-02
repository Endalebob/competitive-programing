# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0,0
            left_cnt, left_sum = dfs(node.left)
            right_cnt, right_sum = dfs(node.right)
            self.ans += ((left_sum+right_sum+node.val)//(left_cnt+right_cnt+1)) == node.val
            return left_cnt+right_cnt+1,left_sum+right_sum+node.val
        dfs(root)
        return self.ans