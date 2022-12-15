class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        if not k:
            return max(vals)
        value = {}
        graph = {}
        sum_ = defaultdict(int)
        for i in range(len(vals)):
            value[i] = vals[i]
        for i,j in edges:
            if i in graph:
                if len(graph[i]) == k:
                    if value[j] > graph[i][0]:
                        sum_[i] += value[j]
                        sum_[i] -= heapq.heappop(graph[i])
                        heapq.heappush(graph[i],value[j])
                elif value[j] > 0:
                    sum_[i] += value[j]
                    heapq.heappush(graph[i],value[j])
            else:
                graph[i] = []
                heapq.heapify(graph[i])
                if value[j] > 0:
                    sum_[i] += value[j]
                    heapq.heappush(graph[i],value[j])
            i,j = j,i
            if i in graph:
                if len(graph[i]) == k:
                    if value[j] > graph[i][0]:
                        sum_[i] += value[j]
                        sum_[i] -= heapq.heappop(graph[i])
                        heapq.heappush(graph[i],value[j])
                elif value[j] > 0:
                    sum_[i] += value[j]
                    heapq.heappush(graph[i],value[j])
            else:
                graph[i] = []
                heapq.heapify(graph[i])
                if value[j] > 0:
                    sum_[i] += value[j]
                    heapq.heappush(graph[i],value[j])
            
        ans = max(vals)
        for i in sum_:
            ans = max(ans,sum_[i]+value[i])
        return ans