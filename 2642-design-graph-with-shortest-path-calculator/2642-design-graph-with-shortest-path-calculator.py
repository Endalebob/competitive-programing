class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for f,t,w in edges:
            self.graph[f].append((t,w))
        

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1],edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        if not node1 in self.graph:
            return -1
        heap = [(0,node1)]
        heapq.heapify(heap)
        vstd = set()
        while heap:
            w,node = heapq.heappop(heap)
            vstd.add(node)
            if node == node2:
                return w
            for i,we in self.graph[node]:
                if i not in vstd:
                    heapq.heappush(heap,(w+we,i))
        return -1
            
            
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)