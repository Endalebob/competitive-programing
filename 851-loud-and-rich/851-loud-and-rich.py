class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        finished = set()
        graph = defaultdict(list)
        n = 0
        ret = [-1 for i in range(len(quiet))]
        for i in richer:
            graph[i[1]].append(i[0])
        def dfs(i):
            if ret[i] == -1:
                ret[i] = i
                for ii in graph[i]:
                    m = dfs(ii)
                    if quiet[m] < quiet[ret[i]]:
                        ret[i] = m
            return ret[i]
        return map(dfs,range(len(quiet)))