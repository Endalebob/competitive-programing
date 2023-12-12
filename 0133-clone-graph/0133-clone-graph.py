"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, nodes: Optional['Node']) -> Optional['Node']:
        if not nodes:
            return
        node_list = defaultdict(int)
        def dfs(node):
            if node.val in node_list:
                return node_list[node.val]
            node_list[node.val] = Node(val=node.val, neighbors=[])
            for i in node.neighbors:
                node_list[node.val].neighbors.append(dfs(i))
            return node_list[node.val]
        return dfs(nodes)