# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        child = deque()
        child.append(root)
        ans = []
        while child:
            temp = deque()
            maxx = child[0].val
            for i in child:
                if i.val>maxx:
                        maxx = i.val
                if i.right:
                    temp.append(i.right)
                if i.left:
                    temp.append(i.left)
            ans.append(maxx)
            child = temp
        return ans
                    
            