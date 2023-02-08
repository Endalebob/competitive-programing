class Solution:
    def restoreArray(self, adjacentPairs):
        adj_list = defaultdict(list)
        for u, v in adjacentPairs:
            adj_list[u].append(v)
            adj_list[v].append(u)
        ans = [next(k for k, v in adj_list.items() if len(v) == 1)]
        stack, visited = [adj_list[ans[0]]], set(ans)
        while stack:
            neighbors = stack.pop()
            for v in neighbors:
                if v in visited:
                    continue
                ans.append(v)
                stack.append(adj_list[v])
                visited.add(v)
        return ans
