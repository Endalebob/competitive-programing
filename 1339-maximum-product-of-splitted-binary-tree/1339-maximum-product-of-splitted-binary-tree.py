# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        ans = set()
        def dfs(root):
            if not root:
                return 0
            val = root.val + dfs(root.right) + dfs(root.left)
            ans.add(val)
            return val
        dfs(root)
        ans = sorted(list(ans))
        ret = 0
        for i in ans:
            ret = max(ret,i*(ans[-1]-i))
        return ret % (10**9+7)