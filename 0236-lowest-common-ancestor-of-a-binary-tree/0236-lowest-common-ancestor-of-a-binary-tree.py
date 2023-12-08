# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', a: 'TreeNode', b: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Check if the current node matches one of the target nodes
            mid = (node == a) or (node == b)
            
            # Calculate the total nodes found in left, right, and current node
            total_nodes = left + right + mid
            
            if total_nodes > 1:
                self.ans = node  # Update the lowest common ancestor
            
            # Return True if at least one target node is found in the subtree
            return total_nodes > 0
        
        dfs(root)
        return self.ans
