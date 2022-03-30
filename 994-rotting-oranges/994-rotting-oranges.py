class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        neighbour = [[0,1],[0,-1],[1,0],[-1,0]]
        isValid = lambda r,c : 0<= r < row and 0<=c<col
        deq = deque()
        checked = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    deq.append([i,j,0])
        ans = 0
        while deq:
            ans = deq[-1][-1]
            current = deq.popleft()
            for i in neighbour:
                r,c = current[0]+i[0],current[1]+i[1]
                if isValid(r,c) and grid[r][c] == 1:
                    grid[r][c] = 2
                    deq.append([r,c,current[-1]+1])
        for i in grid:
            if 1 in i:
                return -1
        return ans