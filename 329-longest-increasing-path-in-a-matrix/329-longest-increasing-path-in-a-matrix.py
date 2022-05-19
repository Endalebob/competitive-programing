class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        isValid = lambda r,c: 0<=r<len(matrix) and 0<=c<len(matrix[0])
        makeMove = [[0,1],[0,-1],[1,0],[-1,0]]
        graph = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for move in makeMove:
                    r,c = i + move[0],j+move[1]
                    if isValid(r,c) and matrix[i][j]<matrix[r][c]:
                        graph[(i,j)].add((r,c))
        vstd = defaultdict(int)
        def dfs(ii):
            if len(graph[ii]) == 0:
                vstd[ii] = 1
                return vstd[ii]
            if ii in vstd:
                return vstd[ii]
            vstd[ii] = 1
            for a in graph[ii]:
                vstd[ii] = max(dfs(a)+1,vstd[ii])
            return vstd[ii]
        ans = 1
        keys = list(graph.keys())
        for i in keys:
            if i in vstd:
                continue      
            ans = max(ans,dfs(i))
        return ans
                    