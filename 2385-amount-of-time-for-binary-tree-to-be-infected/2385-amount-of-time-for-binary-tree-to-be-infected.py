# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.ans = 0
        def recl(r):
            if not r:
                return [0,False]
            right = recl(r.right)
            left = recl(r.left)
            if r.val == start:
                self.ans = max(self.ans,max(right[0],left[0]))
                return [1,True]
            if right[1]:
                self.ans = max(self.ans,right[0]+left[0])
                return [right[0]+1,True]
            if left[1]:
                self.ans = max(self.ans,right[0]+left[0])
                return [left[0]+1,True]
            return [max(right[0],left[0])+1,False]
        recl(root)
        return self.ans
            