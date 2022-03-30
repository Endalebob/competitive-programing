# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        deq = deque()
        deq.append(root)
        flag = 0
        ans = []
        while deq:
            temp = deque()
            temp_ans = []
            for i in deq:
                if i:
                    temp_ans.append(i.val)
                    if i.right:
                        temp.append(i.right)
                    if i.left:
                        temp.append(i.left)
            if flag % 2 == 1:
                ans.append(temp_ans)
            else:
                ans.append(temp_ans[::-1])
            flag += 1
            deq = temp
        return ans