class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        cnt = defaultdict(int)
        
        for i,j in roads:
            graph[i].append(j)
            graph[j].append(i)
            in_degree[i] += 1
            in_degree[j] += 1
        
        deq = deque()
        for i in range(1,len(roads)+1):
            if in_degree[i] == 1:
                deq.append(i)
                cnt[i] += 1
                
                
        ans = 0
        while deq:
            node = deq.popleft()
            ans += int(ceil(cnt[node]/seats))
            for i in graph[node]:
                in_degree[i] -= 1
                cnt[i] += cnt[node]
                if in_degree[i] == 1:
                    if i != 0:
                        cnt[i] += 1
                        deq.append(i)
        return ans
                        