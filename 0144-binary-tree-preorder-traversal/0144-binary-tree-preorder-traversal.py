# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        # def preorder(root):
        #     if not root:
        #         return
        #     output.append(root.val)
        #     preorder(root.left)
        #     preorder(root.right)
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node:
                output.append(curr_node.val)
                stack.append(curr_node.right)
                stack.append(curr_node.left)
        return output
        