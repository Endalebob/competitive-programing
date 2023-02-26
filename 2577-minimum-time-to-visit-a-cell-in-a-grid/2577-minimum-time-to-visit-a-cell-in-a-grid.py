class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        dirc = [[0,1],[1,0],[0,-1],[-1,0]]
        isvalid = lambda r,c : 0<=r<n and 0<=c<m
        if not((isvalid(0,1) and grid[0][1] <= 1) or (isvalid(1,0) and grid[1][0]<=1)):
            return -1
        heap = [[0,(0,0)]]
        heapq.heapify(heap)
        dic = {(0,0):0}
        while heap:
            cost,cell = heapq.heappop(heap)
            for i,j in dirc:
                ni,nj = i+cell[0],j+cell[1]
                if isvalid(ni,nj):
                    if grid[ni][nj] > cost:
                        val = grid[ni][nj]+1
                        if (grid[ni][nj]-cost) % 2:
                            val -= 1
                    else:
                        val = cost+1
                    if (ni,nj) in dic:
                        if dic[(ni,nj)] <= val:
                            continue
                    dic[(ni,nj)] = val
                    heapq.heappush(heap,[val,(ni,nj)])            
        return dic[(n-1,m-1)]