# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(r,flag):
            if flag == 1: 
                if not r.right:
                    r.right = TreeNode(val = val)
                    return
                if r.right.val > val:
                    dfs(r.right,1-flag)
                    return
                dfs(r.right,flag)
            else:
                if not r.left:
                    r.left = TreeNode(val = val)
                    return
                if r.left.val < val:
                    dfs(r.left,1-flag)
                    return
                dfs(r.left,flag)
        if not root:
            return TreeNode(val=val)
        if root.val>val:
            dfs(root,0)
        else:
            dfs(root,1)
        return root
            