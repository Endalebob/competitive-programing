class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j,r,c,ans):
            self.ans += 1
            self.not_include.append([i,j])
            if j+1<c and grid[i][j+1] == 1 and [i,j+1] not in self.not_include:
                dfs(i,j+1,r,c,ans)
            if j-1>=0 and grid[i][j-1] == 1 and [i,j-1] not in self.not_include:
                dfs(i,j-1,r,c,ans)
            if i+1<r and grid[i+1][j] == 1 and [i+1,j] not in self.not_include:
                dfs(i+1,j,r,c,ans)
            if i-1>=0 and grid[i-1][j] == 1 and [i-1,j] not in self.not_include:
                dfs(i-1,j,r,c,ans)
            return ans
        answer = 0
        self.not_include = []
        row = len(grid)
        column = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and [i,j] not in self.not_include:
                    self.ans = 0
                    area = dfs(i,j,row,column,0)
                    answer = max(answer,self.ans)
        return answer
                    
        
            