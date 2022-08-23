class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        isValid = lambda r,c : 0<=r<row and 0<=c<col
        if grid[0][0] == 0:
            heap = [[1,(0,0)]]
        else:
            heap = []
        heapq.heapify(heap)
        vstd = set()
        dirc = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        while heap:
            curr = heapq.heappop(heap)
            if curr[1] in vstd:
                continue
            else:
                vstd.add(curr[1])
            if curr[1] == (row-1,col-1):
                return curr[0]
            for i in dirc:
                r,c = curr[1][0]+i[0],curr[1][1]+i[1]
                if isValid(r,c) and grid[r][c] == 0:
                    if (r,c) not in vstd:
                        heapq.heappush(heap,[curr[0]+1,(r,c)])
        return -1
            