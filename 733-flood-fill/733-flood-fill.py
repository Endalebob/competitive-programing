class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        begin = image[sr][sc]
        if begin == color:
            return image
        row,col = len(image),len(image[0])
        is_valid = lambda r,c: 0<=r<row and 0<=c<col
        dirc = [0,1,0,-1,0]
        vstd = set()
        def rec(r,c):
            if (r,c) in vstd:
                return
            vstd.add((r,c))
            for i in range(4):
                nr,nc = r+dirc[i],c+dirc[i+1]
                if is_valid(nr,nc) and image[nr][nc] == image[sr][sc]:
                    rec(nr,nc)
            image[r][c] = color
        rec(sr,sc)
        return image
            
        