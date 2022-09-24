# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> int:
        if not root:
            return 0
        self.ans = 0
        dic = defaultdict(int)
        all_values = []
        def rec(r):
            s = r.val
            dic = defaultdict(int)
            for i in all_values[::-1]:
                s += i
                dic[s] +=1
            dic[r.val] += 1
            self.ans += dic[t]
            all_values.append(r.val)
            if r.right:
                rec(r.right)
            if r.left:
                rec(r.left)
            all_values.pop()
        rec(root)
        return self.ans