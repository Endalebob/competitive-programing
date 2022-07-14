class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        tot = set(range(n))
        incoming = set()
        for i in edges: incoming.add(i[1])
        return tot-incoming