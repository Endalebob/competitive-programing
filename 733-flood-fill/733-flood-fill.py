class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        wanted = image[sr][sc]
        column_length = len(image[sr])
        row_length = len(image)
        hold = []
        return self.dfs(image,sr,sc,newColor,wanted,row_length,column_length,hold)
    def dfs(self,image,i,j,new,old,r,l,hold):
        image[i][j] = new
        hold.append([i,j])
        if j+1<l and image[i][j+1] == old and [i,j+1] not in hold:
            self.dfs(image,i,j+1,new,old,r,l,hold)
        if j-1>=0 and image[i][j-1] == old and [i,j-1] not in hold:
            self.dfs(image,i,j-1,new,old,r,l,hold)
        if i+1<r and image[i+1][j] == old and [i+1,j] not in hold:
            self.dfs(image,i+1,j,new,old,r,l,hold)
        if i-1>=0 and image[i-1][j] == old and [i-1,j] not in hold:
            self.dfs(image,i-1,j,new,old,r,l,hold)
        return image
        

        