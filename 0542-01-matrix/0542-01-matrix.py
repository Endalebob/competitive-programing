class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        ans = [[-1 for i in range(m)] for j in range(n)]
        dirc = ((0,1),(0,-1),(1,0),(-1,0))
        isvalid = lambda r,c: 0<=r<n and 0<=c<m and ans[r][c] == -1
        que = deque()
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    ans[i][j] = 0
                    que.append((i,j))
        while que:
            for i in range(len(que)):
                r,c = que.popleft()
                for a,b in dirc:
                    nr,nc = r+a,c+b
                    if isvalid(nr,nc):
                        que.append((nr,nc))
                        ans[nr][nc] = ans[r][c] + 1
        return ans