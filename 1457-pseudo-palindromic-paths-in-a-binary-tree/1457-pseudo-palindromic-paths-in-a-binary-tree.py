# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(r,lis):
            lis[r.val] += 1
            if r.left:
                dfs(r.left,lis)
            if r.right:
                dfs(r.right,lis)
            if not r.left and not r.right:
                temp = 0
                for i in lis:
                    if i % 2 == 1:
                        temp += 1
                if temp < 2:
                    self.ans += 1
            lis[r.val] -= 1
        dfs(root,[0]*10)
        return self.ans