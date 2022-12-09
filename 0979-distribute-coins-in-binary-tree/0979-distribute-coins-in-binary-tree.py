# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root,ans):
            if not root: return 0
            left,right = dfs(root.left,ans),dfs(root.right,ans)
            ans[0] += abs(left) + abs(right)
            return root.val-1+left+right
        ans = [0]
        dfs(root,ans)
        return ans[0]