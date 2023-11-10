class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        count = defaultdict(int)
        for i,j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)
            count[i] += 1
            count[j] += 1
        start = 0
        for i in count:
            if count[i] == 1:
                start = i
                break
        ans = []
        que = [start]
        vstd =set()
        while que:
            curr = que.pop()
            vstd.add(curr)
            for i in graph[curr]:
                if i not in vstd:
                    que.append(i)
            ans.append(curr)
        return ans
                
                