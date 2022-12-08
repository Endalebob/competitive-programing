# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root,num):
            if not root:
                return 1
            m = dfs(root.left,num)
            n = dfs(root.right,num)
            if m == 1 and n==1:
                num.append(root.val)
            return m+n+1
        num1 = []
        dfs(root1,num1)
        num2 = []
        dfs(root2,num2)
        return num1 == num2