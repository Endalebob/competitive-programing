# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def rec(r,lis,curr): 
            lis.append(r.val)
            if r.right and r.left:
                rec(r.right,lis,curr+r.val)
                rec(r.left,lis,curr+r.val)
            elif r.right:
                rec(r.right,lis,curr+r.val)
            elif r.left:
                rec(r.left,lis,curr+r.val)
            else:
                if curr+r.val == t:
                    ans.append(deepcopy(lis))
            lis.pop()
        rec(root,[],0)
        return ans
                