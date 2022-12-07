# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        nums = []
        def dfss(root):
            if not root:
                return
            dfss(root.left)
            nums.append(root.val)
            dfss(root.right)
        dfss(root)
        
        nums.append(val)
        def dfs(l,r):
            if l>=r:
                return 
            v = l
            for i in range(l,r):
                if nums[i] > nums[v]:
                    v = i
            tree = TreeNode(val = nums[v],left = dfs(l,v),right = dfs(v+1,r))
            return tree
        return dfs(0,len(nums))