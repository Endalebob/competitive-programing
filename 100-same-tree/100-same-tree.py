# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        deqp, deqq = deque(),deque()
        if p and q and p.val == q.val:
            deqp.append(p)
            deqq.append(q)
        else:
            return p == q
        while deqp and deqq:
            pp,qq = deqp.popleft(), deqq.popleft()
            if pp.val != qq.val:
                return False
            if pp.left:
                if not qq.left:
                    return False
                deqp.append(pp.left)
            if pp.right:
                if not qq.right:
                    return False
                deqp.append(pp.right)
            if qq.left:
                if not pp.left:
                    return False
                deqq.append(qq.left)
            if qq.right:
                if not pp.right:
                    return False
                deqq.append(qq.right)
        return deqp == deqq