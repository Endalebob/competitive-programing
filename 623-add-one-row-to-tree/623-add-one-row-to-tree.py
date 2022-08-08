# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val = val,left = root)
        dep = 2
        deq = deque()
        deq.append(root)
        while deq:
            temp = deque()
            if dep == depth:
                for i in deq:
                    new_r = TreeNode(val = val,right = i.right)
                    new_l = TreeNode(val = val,left = i.left)
                    i.left = new_l
                    i.right = new_r
            for i in deq:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            deq = temp
            dep += 1
        return root