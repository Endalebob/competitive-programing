# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        hold = [root]
        while hold:
            summ = 0
            for i in hold:
                if i:
                    summ += i.val
            ans.append(summ/len(hold))
            temp = []
            for i in hold:
                if i.right:
                    temp.append(i.right)
                if i.left:
                    temp.append(i.left)
            hold = temp
        return ans
            