"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, nodee: Optional['Node']) -> Optional['Node']:
        if not nodee:
            return nodee
        vstd = {}
        def dfs(node):
            if node.val in vstd:
                return vstd[node.val]
            vstd[node.val] = Node(node.val,[])
            for neigh in node.neighbors:
                vstd[node.val].neighbors.append(dfs(neigh))
            return vstd[node.val]
        return dfs(nodee)
            