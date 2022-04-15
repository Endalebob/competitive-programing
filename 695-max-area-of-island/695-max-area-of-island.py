class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        isValid = lambda r,c: 0<=r<len(grid) and 0<=c<len(grid[0])
        nxt = [0,1,0,-1,0]
        vstd = set()
        def dfs(r,c):
            self.ans += 1
            vstd.add((r,c))
            for j in range(len(nxt)-1):
                if isValid(r+nxt[j],c+nxt[1+j]) and (r+nxt[j],c+nxt[1+j]) not in vstd and grid[r+nxt[j]][c+nxt[1+j]] == 1:
                    dfs(r+nxt[j],c+nxt[1+j])
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in vstd and grid[i][j] == 1:
                    self.ans = 0
                    dfs(i,j)
                    answer = max(answer,self.ans)
        return answer