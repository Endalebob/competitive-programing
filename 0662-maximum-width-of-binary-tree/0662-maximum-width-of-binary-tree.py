# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = {}
        def dp(root,depth,curr):
            if not root:
                return
            if depth in level:
                level[depth][0] = max(level[depth][0],curr)
                level[depth][1] = min(level[depth][1],curr)
            else:
                level[depth] = [curr,curr]
            dp(root.left,depth+1,2*curr)
            dp(root.right,depth+1,2*curr+1)
        dp(root,1,1)
        ans = 0
        for i in level:
            ans = max(ans,level[i][0]-level[i][1])
        return ans+1