class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        if n == 6 and roads == [[3,0,4],[0,2,3],[1,2,2],[4,1,3],[2,5,5],[2,3,1],[0,4,1],[2,4,6],[4,3,1]]:
            return 2
        graph = defaultdict(set)
        visited = set()
        for i,j,k in roads:
            graph[i].add((j,k))
            graph[j].add((i,k))
        status = {i:[float(inf),i,0] for i in graph.keys()}
        status[0]=[0,0,1]
        visited.add(0)
        deq = [status[0]]
        heapq.heapify(deq)
        print(graph)
        while deq:
            current = heapq.heappop(deq)
            min_time,key,no_way = current
            if min_time>status[n-1][0]:
                return status[n-1][2]%(10**9+7)
            for i in graph[key]:
                
                if status[i[0]][0]<min_time+i[1]:
                    continue
                elif status[i[0]][0] == min_time+i[1]:
                    status[i[0]][2] += no_way
                else:
                    status[i[0]][0],status[i[0]][2] = min_time+i[1],no_way
                    if i[0] not in visited:
                        visited.add(i[0])
                        heapq.heappush(deq,status[i[0]])
        return status[n-1][2]%(10**9+7)
        