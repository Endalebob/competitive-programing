class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        neighbour = defaultdict(list)
        degree = defaultdict(int)
        isvalid = lambda r,c: 0<=r<n and 0<=c<m and grid[r][c] == 1
        dirc = [[0,1],[1,0],[0,-1],[-1,0]]
        
        def dfs(i,j):
            ans = 1
            vstd.add((i,j))
            for ii,jj in dirc:
                r,c = i+ii,j+jj
                if isvalid(r,c) and (r,c) not in vstd:
                    ans += dfs(r,c)
            return ans

        
        current_count = 0
        holla = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    holla.append([i,j])
                    current_count += 1
                    
        if not current_count:
            return 0
                    
        vstd = set()          
        if dfs(holla[0][0],holla[0][1]) < current_count:
            return 0
        
        if current_count == 1:
            return 1
        vstd = set()
        grid[holla[0][0]][holla[0][1]] = 0
        if dfs(holla[1][0],holla[1][1]) < current_count-1:
            return 1 
        grid[holla[0][0]][holla[0][1]] = 0
        
        for k in range(1,current_count):
            i,j = holla[k]
            grid[i][j] = 0
            vstd = set() 
            if dfs(holla[0][0],holla[0][1]) < current_count-1:
                return 1
            grid[i][j] = 1
        return 2
            
                      
                
        
        