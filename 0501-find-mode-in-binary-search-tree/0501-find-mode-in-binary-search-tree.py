# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        self.ans = 0
        def dfs(node):
            if not node:
                return
            count[node.val] += 1
            self.ans = max(self.ans,count[node.val])
            dfs(node.left)
            dfs(node.right)
        ans = []
        dfs(root)
        for i in count:
            if count[i] == self.ans:
                ans.append(i)
        return ans