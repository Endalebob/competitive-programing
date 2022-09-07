# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ret = []
        check = set()
        allr = set()
        def dfs(r):
            if not r:
                return ''
            left = dfs(r.left)
            right = dfs(r.right)
            if right:
                ans = str(r.val)+'|'+left+'|'+right
            elif left:
                ans =  str(r.val)+'|'+left
            else:
                ans =  str(r.val)
            if ans in check and ans not in allr:
                ret.append(r)
                allr.add(ans)
            else:
                check.add(ans)
            return '('+ans+')'
        dfs(root)
        return ret
           