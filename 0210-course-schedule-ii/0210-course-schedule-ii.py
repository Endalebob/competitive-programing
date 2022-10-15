class Solution:
    def findOrder(self, c: int, pre: List[List[int]]) -> List[int]:
        graph = defaultdict(int)
        out_going = defaultdict(list)
        for i,v in pre:
            graph[i] += 1
            out_going[v].append(i)
        deq = deque()
        for i in range(c):
            if not graph[i]:
                deq.append(i)
        ans = []
        while deq:
            curr = deq.popleft()
            for i in out_going[curr]:
                graph[i] -= 1
                if graph[i] == 0:
                    deq.append(i)
            ans.append(curr)
        if len(ans) == c:
            return ans
        else: return []
            