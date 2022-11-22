# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], quiries: List[int]) -> List[List[int]]:
        nums = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        inorder(root)
        
        def b_search(target):
            l,r = 0,len(nums)-1
            while l<r:
                m = l+(r-l)//2
                if nums[m] <= target:
                    l = m+1
                else:
                    r = m
            return l
        
        ret = []
        for i in quiries:
            idx = b_search(i)
            ans = [-1,-1]
            if nums[idx-1] == i:
                ans = [i,i]
            else:
                if nums[idx] <= i:
                    ans[0] = nums[idx]
                elif nums[idx-1]<=i:
                    ans[0] = nums[idx-1]
                if nums[idx] >= i:
                    ans[1] = nums[idx]
            ret.append(ans)
        return ret