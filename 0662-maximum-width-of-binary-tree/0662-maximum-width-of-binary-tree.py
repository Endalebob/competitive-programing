# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        deq = deque([[root,0]])
        ans = 0
        while deq:
            ans = max(deq[-1][1] - deq[0][1],ans)
            for i in range(len(deq)):
                curr,pos = deq.popleft()
                if curr.left:
                    deq.append([curr.left,pos*2])
                if curr.right:
                    deq.append([curr.right,pos*2+1])
        return ans+1
        