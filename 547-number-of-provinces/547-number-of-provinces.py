class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(index):
            not_include.append(index)
            for j in range (len(isConnected[index])):
                if isConnected[index][j] == 1 and j not in not_include:
                    dfs(j)
        not_include = []
        ans = 0
        for i in range(len(isConnected)):
            if i not in not_include:
                ans += 1
                dfs(i)
        return ans