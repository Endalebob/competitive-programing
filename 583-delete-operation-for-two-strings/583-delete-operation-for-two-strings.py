class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        grid = [[0 for i in range(m+1)] for f in range(n+1)]
        for i in range(n):
            for j in range(m):
                if word1[j] == word2[i]:
                    grid[i+1][j+1] = grid[i][j] + 1
                else:
                    grid[i+1][j+1] = max(grid[i][j+1],grid[i+1][j])
        return m+n-2*grid[-1][-1]
        