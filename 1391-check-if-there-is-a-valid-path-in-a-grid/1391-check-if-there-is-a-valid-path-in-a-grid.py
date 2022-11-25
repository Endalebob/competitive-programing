class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        isvalid = lambda r,c : 0<=r<n and 0<=c<m
        dirc = {
            1: [(0, -1), (0, 1)] ,
            2: [(-1, 0), (1, 0)] ,
            3: [(0, -1), (1, 0)] ,
            4: [(0, 1), (1, 0)] ,
            5: [(0, -1), (-1, 0)] ,
            6: [(0, 1), (-1, 0)] ,
        }
        
        vstd =set()
        def dfs(r,c):
            vstd.add((r,c))
            if r == n-1 and c == m-1:
                return True
            di = dirc[grid[r][c]]
            for dr,dc in di:
                rr,cc = r+dr,dc+c
                if isvalid(rr,cc) and (rr,cc) not in vstd and (-dr, -dc) in dirc[grid[rr][cc]]:
                    if dfs(rr,cc):
                        return True
            return False
        return dfs(0,0)