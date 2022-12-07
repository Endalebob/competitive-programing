# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root,ans):
            if not root:
                return
            elif low <= root.val <=high:
                ans[0] += root.val
                dfs(root.left,ans)
                dfs(root.right,ans)
            elif low > root.val:
                dfs(root.right,ans)
            else:
                dfs(root.left,ans)
        ans = [0]
        dfs(root,ans)
        return ans[0]