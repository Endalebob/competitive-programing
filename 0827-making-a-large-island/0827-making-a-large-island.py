class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        block = defaultdict(int)
        blocked = defaultdict(set)
        n = len(grid)
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        isvalid = lambda r,c : 0<=r<n and 0<=c<n
        vstd = set()
        idd = 0
        def dfs(i,j,idd):
            block[idd] += 1
            vstd.add((i,j))
            for ii,jj in directions:
                r,c = ii+i,jj+j
                if isvalid(r,c) and (r,c) not in vstd:
                    if grid[r][c] == 0:
                        blocked[(r,c)].add(idd)
                    else:
                        dfs(r,c,idd)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in vstd:
                    idd += 1
                    dfs(i,j,idd)
        if not blocked and grid[0][0] == 1:
            return n*n
        ans = 0
        for key in blocked:
            temp = 0
            for j in blocked[key]:
                temp += block[j]
            ans = max(ans,temp)
        return ans+1