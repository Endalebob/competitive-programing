# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        def dfs(r,x,y):
            ans[(x,y)].append(r.val)
            if r.left:
                dfs(r.left,x-1,y+1)
            if r.right:
                dfs(r.right,x+1,y+1)
        dfs(root,0,0)
        nums = list(ans.keys())
        ret = []
        nums.sort()
        i = 0
        while i<len(nums):
            temp = []
            temp += sorted(ans[nums[i]])
            while i+1<len(nums) and nums[i+1][0] == nums[i][0]:
                i += 1
                temp += sorted(ans[nums[i]])
            ret.append(temp)
            i += 1
        # for i in sorted(nums):
        #     ret.append(sorted(ans[i]))
        return ret