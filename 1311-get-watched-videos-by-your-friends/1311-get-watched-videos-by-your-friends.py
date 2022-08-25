class Solution:
    def watchedVideosByFriends(self, wat: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph = {}
        for i in range(len(friends)):
            graph[i] = friends[i]
        lev = 0
        deq = deque()
        deq.append(id)
        vstd = set()
        vstd.add(id)
        while deq:
            if level == lev:
                break
            temp = deque()
            for i in deq:
                for j in graph[i]:
                    if j not in vstd:
                        vstd.add(j)
                        temp.append(j)
            deq = temp
            lev += 1
        temp = defaultdict(int)
        for i in deq:
            for j in wat[i]:
                temp[j] += 1
        ans = []
        for i in temp:
            ans.append([temp[i],i])
        ans.sort()
        return [i[1] for i in ans]
        
                        