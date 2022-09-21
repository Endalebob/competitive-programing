class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        grid = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:    
                    grid[i+1][j+1] = grid[i][j]+1
                else:
                    grid[i+1][j+1] = max(grid[i][j+1],grid[i+1][j])
        app = []
        i,j = len(text2),len(text1)
        while i > 0 or j > 0:
            if grid[i][j] == grid[i][j-1] and j>0:
                app.append(text1[j-1])
                j -= 1
            elif grid[i][j] == grid[i-1][j]:
                app.append(text2[i-1])
                i -= 1
            else:
                app.append(text2[i-1])
                i -= 1
                j -= 1
        return ''.join(app[::-1])