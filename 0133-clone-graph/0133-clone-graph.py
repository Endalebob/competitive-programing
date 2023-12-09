"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        list_node = defaultdict(int)
        def dfs(nod):
            if nod.val in list_node:
                return list_node[nod.val]
            list_node[nod.val] = Node(val=nod.val,neighbors=[])
            for nigh in nod.neighbors:
                list_node[nod.val].neighbors.append(dfs(nigh))
            return list_node[nod.val]
        return dfs(node)