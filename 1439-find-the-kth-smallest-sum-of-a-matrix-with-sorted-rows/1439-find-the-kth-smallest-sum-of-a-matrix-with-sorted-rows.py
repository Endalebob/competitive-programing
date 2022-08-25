class Solution:
    def kthSmallest(self, grid: List[List[int]], k: int) -> int:
        row,col = len(grid),len(grid[0])
        dirc = [(1,1),(1,0),(1,-1),(-1,-1),(-1,0),(-1,1)]
        hea = []
        s = 0
        for i in range(row):
            s += grid[i][0]
            hea.append([i,0])
        heap = [[s,hea]]
        heapq.heapify(heap)
        ans = 0
        vstd = set()
        while heap:
            summ,idx = heapq.heappop(heap)
            check = tuple(tuple(i) for i in idx)
            if check in vstd:
                continue
            else:
                vstd.add(check)
            ans += 1
            if ans == k:
                return summ
            for i in range(row):
                if idx[i][1]+1<col:
                    m = copy.deepcopy(idx)
                    s = summ-grid[idx[i][0]][idx[i][1]] + grid[idx[i][0]][idx[i][1]+1]
                    m[i][1] += 1
                    heapq.heappush(heap,[s,m])
                