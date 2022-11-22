# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        nums = []
        inorder(root)
        
        
        ret = []
        for i in queries:
            idx = bisect_right(nums,i)
            ans = [-1,-1]
            if idx > 0:
                ans[0] = nums[idx-1]
            if idx <= len(nums):
                if idx>0 and nums[idx-1] == i:
                    ans[1] = nums[idx-1]
                elif idx<len(nums):
                    ans[1] = nums[idx]
            ret.append(ans)
        return ret
                    
                    
                
#         def min_find(root,val):
#             if not root:
#                 return -1
#             if root.val <= val:
#                 return max(root.val,min_find(root.right,val))
#             return min_find(root.left,val)
#         def max_find(root,val):
#             if not root:
#                 return float('inf')
#             if root.val >= val:
#                 return min(root.val,max_find(root.left,val))
#             return max_find(root.right,val)
        
#         ans = []
#         for i in queries:
#             a = max_find(root,i)
#             if a == float('inf'):
#                 a = -1
#             ans.append([min_find(root,i),a])
#         return ans