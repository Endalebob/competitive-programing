# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def val(r):
            if not r: return []
            return val(r.left) + [r.val] + val(r.right)
        ans = val(root)
        a = Counter(ans)
        max_ = max(a.values())
        ret = []
        for i in a:
            if a[i] == max_:
                ret.append(i)
        return ret