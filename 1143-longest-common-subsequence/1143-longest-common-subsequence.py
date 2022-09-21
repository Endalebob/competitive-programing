class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:    
                    grid[i+1][j+1] = grid[i][j]+1
                else:
                    grid[i+1][j+1] = max(grid[i][j+1],grid[i+1][j])
        return grid[-1][-1]