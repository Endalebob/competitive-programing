# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        ans = 0
        self.found=False
        self.dfs(root,ans,targetSum)
        return self.found
    def dfs(self,root,ans,target):
        ans += root.val
        if ans == target and root.right == None and root.left == None:
            self.found=True
            return True
        if root.right:
            self.dfs(root.right,ans,target)
        if root.left:
            self.dfs(root.left,ans,target)
        return False