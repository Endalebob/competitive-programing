class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        row,col = len(grid),len(grid[0])
        isValid = lambda r,c : 0<=r<row and 0<=c<col
        notInclude = set()
        que = deque()
        self.ret = 0
        for i in grid:
            self.ret += i.count(1)
        def dfs(i,j):
            if (i,j) not in notInclude:
                self.ret -= 1
                notInclude.add((i,j))
            for ii in directions:
                r,c = ii[0]+i,ii[1]+j
                if isValid(r,c) and grid[r][c] == 1 and (r,c) not in notInclude:
                    dfs(r,c)
                
        for i in range(row):
            if isValid(i,0) and grid[i][0] == 1 and (i,0) not in notInclude:
                dfs(i,0)
        for i in range(row):
            if isValid(i,col-1) and grid[i][col-1] == 1 and (i,col-1) not in notInclude:
                dfs(i,col-1)
        for j in range(col-2):
            if isValid(0,j+1) and grid[0][j+1] and (0,j+1) not in notInclude:
                dfs(0,j+1)
        for j in range(col-2):
            if isValid(row-1,j+1) and grid[row-1][j+1] and (row-1,j+1) not in notInclude:
                dfs(row-1,j+1)
        return self.ret
        