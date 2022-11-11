class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)


        for prev,next in relations:
            graph[next].append(prev)

        def top_sort(node):
            if node in total:
                return total[node]
            num = 0
            for i in graph[node]:
                num = max(top_sort(i),num)
            total[node] = num + time[node-1]
            return total[node]
        
        
        ans = 0
        total = {}
        for i in range(1,n+1):
            top_sort(i)
            ans = max(ans,total[i])
        return ans