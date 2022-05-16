class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        possible_path = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
        is_valid = lambda r,c : 0 <= r < len(grid) and 0<= c < len(grid[0])
        deq = deque()
        if grid[0][0] == 0:
            deq.append((0,0,1))
            grid[0][0] = 1
        while deq:
            row,col,length = deq.popleft()
            if row == len(grid)-1 and col == len(grid[0])-1:
                return length
            for i in possible_path:
                if is_valid(row+i[0],col+i[1]) and grid[row+i[0]][col+i[1]] == 0:
                    deq.append((row+i[0],col+i[1],length+1))
                    grid[row+i[0]][col+i[1]] = 1
        return -1
                    