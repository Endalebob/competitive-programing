class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        prev = [0]*len(matrix[0])
        curr = [0]*len(matrix[0])
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]:
                    curr[j] += 1
                else:
                    curr[j] = 0
            c = sorted(curr)
            for i in range(len(matrix[0])):
                ans = max(c[i]*(len(matrix[0])-i),ans)
        return ans