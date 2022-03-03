# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        for_loop = deque()
        if root:
            for_loop.append(root)
        else:
            return True
        while for_loop:
            for i in range(len(for_loop)):
                if for_loop[i] and for_loop[-1-i]:
                    if for_loop[i].val != for_loop[-1-i].val:
                        return False
                elif for_loop[i] == None and for_loop[-1-i] == None:
                    continue
                else:
                    return False
                    
            temp = deque()
            while for_loop:
                a = for_loop.pop()
                if a:
                    temp.append(a.left)
                if a:
                    temp.append(a.right)
            for_loop = temp
        return True
            
            
                
        