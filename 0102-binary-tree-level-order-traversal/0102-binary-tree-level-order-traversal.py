# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deq = deque()
        if root:
            deq.append([root])
        ans = []
        while deq:
            curr = deq.popleft()
            temp = []
            for i in curr:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if temp:
                deq.append(temp)
            new = []
            for i in curr:
                new.append(i.val)
            ans.append(new)
        return ans
                    