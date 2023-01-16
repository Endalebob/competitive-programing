# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        deq = deque([root])
        ans = []
        while deq:
            temp = []
            for i in range(len(deq)):
                curr = deq.popleft()
                temp.append(curr.val)
                if curr.left:
                    deq.append(curr.left)
                if curr.right:
                    deq.append(curr.right)
            ans.append(temp)
        return ans[::-1]
        