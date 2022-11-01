class Solution:
    def countBattleships(self, matrix: List[List[str]]) -> int:
        Component_count = 0
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        row = len(matrix)
        col = len(matrix[0])

        isvalid = lambda r,c : 0<=r<row and 0<=c<col and matrix[r][c] == 'X'
        def dfs(i,j):
            visited.add((i,j))
            for xi,yi in directions:
                r,c = i+xi,j+yi
                if isvalid(r,c) and (r,c) not in visited:
                    dfs(r,c)
        visited = set()
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 'X' and (r,c) not in visited:
                    dfs(r,c)
                    Component_count = Component_count+1
        return Component_count