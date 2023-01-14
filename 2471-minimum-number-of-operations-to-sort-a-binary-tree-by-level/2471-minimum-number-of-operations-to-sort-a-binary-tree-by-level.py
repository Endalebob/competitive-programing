# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        deq = deque([root])
        while deq:
            temp = []
            for i in range(len(deq)):
                curr = deq.popleft()
                temp.append(curr.val)
                if curr.left:
                    deq.append(curr.left)
                if curr.right:
                    deq.append(curr.right)
            ind = {temp[i]:i for i in range(len(temp))}
            k = sorted(temp)
            
            for i in range(len(temp)):
                if ind[k[i]] != i:
                    ind[temp[i]] = ind[k[i]]
                    temp[ind[k[i]]] = temp[i]
                    cnt += 1
        return cnt
                    