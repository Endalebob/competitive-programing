# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deq = deque()
        ans = []
        deq.append(root)
        while deq:
            hold = []
            temp = deque()
            while deq:
                curr = deq.popleft()
                if curr:
                    hold.append(curr.val)
                    if curr.left:
                        temp.append(curr.left)
                    if curr.right:
                        temp.append(curr.right)
            if hold:
                ans.append(hold)
            deq = temp
        return ans
                