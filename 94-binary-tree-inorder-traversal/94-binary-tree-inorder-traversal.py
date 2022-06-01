# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node: return
            if not node.left and not node.right:
                return [node.val]
            ans = [node.val]
            if node.right:
                ans = ans + dfs(node.right)
            if node.left:
                ans = dfs(node.left) + ans
            return ans
        return dfs(root)
            