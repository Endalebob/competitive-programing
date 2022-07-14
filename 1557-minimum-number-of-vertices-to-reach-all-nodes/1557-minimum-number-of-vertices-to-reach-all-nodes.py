class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        total_edge = set(range(n))
        incoming = set()
        for i in edges: incoming.add(i[1])
        return total_edge - incoming