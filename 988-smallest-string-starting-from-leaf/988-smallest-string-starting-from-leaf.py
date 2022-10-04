# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = '~'
        def dfs(r,s):
            if not r:
                return
            if not r.left and not r.right:
                self.ans = min(self.ans,str(chr(ord('a')+r.val))+s)
                return
            dfs(r.left,str(chr(ord('a')+r.val))+s)
            dfs(r.right,str(chr(ord('a')+r.val))+s)
        dfs(root,'')
        return self.ans
        