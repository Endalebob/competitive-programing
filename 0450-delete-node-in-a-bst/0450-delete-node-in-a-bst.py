# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def left(root):
            root = root.left
            while root.right:
                root = root.right
            return root.val
        def right(root):
            root = root.right
            while root.left:
                root = root.left
            return root.val
        def delete(root,key):
            if not root:
                return None
            if root.val < key:
                root.right = delete(root.right,key)
            elif root.val > key:
                root.left = delete(root.left,key)
            else:
                if not root.left and not root.right:
                    root = None
                elif root.right:
                    root.val = right(root)
                    root.right = delete(root.right,root.val)
                else:
                    root.val = left(root)
                    root.left = delete(root.left,root.val)
            return root
        return delete(root,key)