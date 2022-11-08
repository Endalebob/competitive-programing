# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dfs(root,left,right):
            if not root:
                return True
            if not (root.val<right and root.val>left):
                return False
            return dfs(root.left,left,root.val) and dfs(root.right,root.val,right)
        @lru_cache(None)
        def dfsSum(root):
            if not root:
                return 0
            return root.val + dfsSum(root.left) + dfsSum(root.right)
        @lru_cache(None)
        def max_(root):
            if not root:
                return 0
            if dfs(root,-float('inf'),float('inf')):
                return max(max_(root.left),max_(root.right),dfsSum(root))
            return max(max_(root.left),max_(root.right))
        return max(0,max_(root))