# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node,ans):
            if not node:
                return 0
            left = dfs(node.left,ans)
            right = dfs(node.right,ans)
            ans[0] = max(ans[0],left+right)
            return max(left,right)+1
        ans = [0]
        dfs(root,ans)
        return ans[0]