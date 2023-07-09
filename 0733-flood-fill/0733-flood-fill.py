class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirc = ((0,1),(0,-1),(1,0),(-1,0))
        n,m,colo = len(image),len(image[0]),image[sr][sc]
        isvalid = lambda r,c: 0<=r<n and 0<=c<m and image[r][c] == colo
        def dfs(r,c):
            image[r][c] = color
            for i,j in dirc:
                nr,nc = i+r,j+c
                if isvalid(nr,nc):
                    dfs(nr,nc)
        if image[sr][sc] == color:
            return image
        dfs(sr,sc)
        return image