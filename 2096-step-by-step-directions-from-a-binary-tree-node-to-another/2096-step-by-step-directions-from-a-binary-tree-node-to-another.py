# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], s: int, d: int) -> str:
        graph = defaultdict(list)
        deq = deque([root])
        while deq:
            curr = deq.popleft()
            if curr.left:
                graph[curr.left.val].append((curr.val,'U'))
                graph[curr.val].append((curr.left.val,'L'))
                deq.append(curr.left)
            if curr.right:
                graph[curr.right.val].append((curr.val,'U'))
                graph[curr.val].append((curr.right.val,'R'))
                deq.append(curr.right)
        deq = deque([(s,'')])
        vstd = {s}
        while deq:
            node,path = deq.popleft()
            if node == d:
                return path
            for i,j in graph[node]:
                if i not in vstd:
                    vstd.add(i)
                    deq.append((i,path+j))
            